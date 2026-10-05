"""Independent recomputation from the exported transformed rows using stdlib math."""
from pathlib import Path
import csv
import hashlib
import json
import math
import io
import subprocess
import tempfile
import zipfile
from datetime import datetime
from openpyxl import load_workbook

ROOT = Path(__file__).resolve().parent
CASE = ROOT.parents[1]
SPEC = CASE / "daily_competing_mechanisms_spec.md"
SPEC_SHA256 = "c332089e04af3e30418b72b21242c45e866d857a546a0aed51ba0c9369c8a9de"
REGRESSORS = [
    ("H1", "d_DGS2_bp"), ("H2", "d_DFII10_bp"), ("H3", "d_T10YIE_bp"),
    ("H4", "d_ACMTP10_bp"), ("H5", "d_DGS30_bp"),
]


def corr(x, y):
    mx, my = sum(x) / len(x), sum(y) / len(y)
    numerator = sum((a - mx) * (b - my) for a, b in zip(x, y))
    return numerator / math.sqrt(sum((a - mx) ** 2 for a in x) * sum((b - my) ** 2 for b in y))


def regress(y, x):
    mx, my = sum(x) / len(x), sum(y) / len(y)
    coefficient = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sum((a - mx) ** 2 for a in x)
    intercept = my - coefficient * mx
    fitted = [intercept + coefficient * a for a in x]
    sse = sum((a - b) ** 2 for a, b in zip(y, fitted))
    sst = sum((a - my) ** 2 for a in y)
    return coefficient, intercept, 1 - sse / sst


def main():
    assert hashlib.sha256(SPEC.read_bytes()).hexdigest() == SPEC_SHA256
    manifest = json.loads((ROOT / "source_manifest.json").read_text())
    for item in manifest:
        raw_path = ROOT / item["file"]
        assert hashlib.sha256(raw_path.read_bytes()).hexdigest() == item["sha256"]
    rows = list(csv.DictReader((ROOT / "common_sample_changes.csv").open()))
    # Rebuild the intersection and differences from raw sources, independently
    # of the pandas join/diff implementation. Spreadsheet conversion is shared.
    raw = ROOT.parent / "taylor93" / "raw"
    with zipfile.ZipFile(raw / "rates.csv") as archive:
        fred_rows = list(csv.DictReader(io.StringIO(archive.read("daily.csv").decode())))
    columns = ["DGS10", "DGS2", "DFII10", "T10YIE", "DGS30"]
    fred = {}
    for row in fred_rows:
        if "2006-02-09" <= row["observation_date"] <= "2026-09-25":
            if all(row[c] not in ("", ".") for c in columns):
                assert row["observation_date"] not in fred
                fred[row["observation_date"]] = {c: float(row[c]) for c in columns}
    with tempfile.TemporaryDirectory(prefix="case002_independent_") as tmp:
        subprocess.run(["/Users/selenakim/.cache/codex-runtimes/codex-primary-runtime/dependencies/bin/override/soffice",
                        "--headless", "--convert-to", "xlsx", "--outdir", tmp,
                        str(raw / "ACMTermPremium.xls")], check=True, capture_output=True)
        workbook = load_workbook(Path(tmp) / "ACMTermPremium.xlsx", read_only=True, data_only=True)
        sheet = workbook["ACM Daily"].iter_rows(values_only=True)
        header = list(next(sheet))
        acm = {}
        for values in sheet:
            date_value, value = values[header.index("DATE")], values[header.index("ACMTP10")]
            if date_value is not None and value is not None:
                day = datetime.strptime(date_value, "%d-%b-%Y").strftime("%Y-%m-%d")
                assert day not in acm
                acm[day] = float(value)
        workbook.close()
    dates = sorted(set(fred) & set(acm))
    assert len(dates) == len(rows) + 1
    for previous, current, row in zip(dates, dates[1:], rows):
        assert row["date"] == current and row["prior_common_date"] == previous
        expected_gap = (datetime.fromisoformat(current) - datetime.fromisoformat(previous)).days
        assert int(row["interval_calendar_days"]) == expected_gap
        for column in columns + ["ACMTP10"]:
            current_value = acm[current] if column == "ACMTP10" else fred[current][column]
            previous_value = acm[previous] if column == "ACMTP10" else fred[previous][column]
            assert abs(float(row[column]) - current_value) < 1e-9
            assert abs(float(row[f"d_{column}_bp"]) - 100 * (current_value - previous_value)) < 1e-9
    reported = {r["hypothesis"]: r for r in csv.DictReader((ROOT / "first_pass_metrics.csv").open())}
    assert rows[0]["date"] == "2006-02-10" and rows[-1]["date"] == "2026-09-25"
    y = [float(r["d_DGS10_bp"]) for r in rows]
    checks = []
    for hypothesis, column in REGRESSORS:
        x = [float(r[column]) for r in rows]
        correlation = corr(y, x)
        coefficient, intercept, r_squared = regress(y, x)
        expected = reported[hypothesis]
        differences = {
            "correlation": abs(correlation - float(expected["correlation_with_d_DGS10"])),
            "r_squared": abs(r_squared - float(expected["ols_r_squared"])),
            "coefficient": abs(coefficient - float(expected["coefficient"])),
            "intercept": abs(intercept - float(expected["intercept_bp"])),
        }
        assert max(differences.values()) < 1e-9
        assert int(expected["N"]) == len(rows)
        checks.append({"hypothesis": hypothesis, "max_abs_metric_difference": max(differences.values())})
    identity = max(abs(float(r["d_DGS10_bp"]) - float(r["d_DFII10_bp"]) - float(r["d_T10YIE_bp"])) for r in rows)
    assert identity < 1e-9
    result = {
        "status": "passed", "method": "stdlib csv/math recomputation; no pandas, numpy, or regression package",
        "raw_hashes_rechecked": True,
        "raw_intersection_and_all_transformations_recomputed": True,
        "independence_limit": "Both readers use LibreOffice to convert XLS; primary uses pandas and numpy, check uses openpyxl and stdlib math.",
        "row_count": len(rows), "first_change_date": rows[0]["date"], "last_change_date": rows[-1]["date"],
        "hypothesis_checks": checks, "max_abs_identity_residual_bp": identity,
        "absolute_metric_tolerance": 1e-9, "specification_sha256_after_calculation": SPEC_SHA256,
    }
    (ROOT / "independent_validation.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
