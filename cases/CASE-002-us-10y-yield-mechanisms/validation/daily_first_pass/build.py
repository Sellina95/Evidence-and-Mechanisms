"""Frozen CASE-002 daily first pass. Research-only; no production imports."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import io
import json
import math
import platform
import subprocess
import tempfile
import zipfile

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent
CASE = ROOT.parents[1]
SPEC = CASE / "daily_competing_mechanisms_spec.md"
RAW = CASE / "validation" / "taylor93" / "raw"
START = pd.Timestamp("2006-02-09")
END = pd.Timestamp("2026-09-25")
SPEC_SHA256 = "c332089e04af3e30418b72b21242c45e866d857a546a0aed51ba0c9369c8a9de"
SOFFICE = Path("/Users/selenakim/.cache/codex-runtimes/codex-primary-runtime/dependencies/bin/override/soffice")

SERIES = ["DGS10", "DGS2", "DFII10", "T10YIE", "ACMTP10", "DGS30"]
REGRESSORS = [
    ("H1", "Policy-path / front-end repricing proxy", "d_DGS2_bp"),
    ("H2", "Real-yield repricing; mechanical component", "d_DFII10_bp"),
    ("H3", "Inflation compensation; mechanical component", "d_T10YIE_bp"),
    ("H4", "Term-premium repricing; MODEL ESTIMATE", "d_ACMTP10_bp"),
    ("H5", "Long-end / curve-specific repricing proxy", "d_DGS30_bp"),
]

SOURCES = [
    {"file": "../taylor93/raw/rates.csv", "series": "DGS2,DGS10,DGS30,DFII10,T10YIE",
     "url": "https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF,DGS2,DGS10,DGS30,DFII10,T10YIE",
     "source": "Federal Reserve Board H.15 via FRED; T10YIE derived by St. Louis Fed",
     "frequency": "daily", "units": "percent"},
    {"file": "../taylor93/raw/ACMTermPremium.xls", "series": "ACMTP10",
     "url": "https://www.newyorkfed.org/medialibrary/media/research/data_indicators/ACMTermPremium.xls",
     "landing_page": "https://www.newyorkfed.org/research/data_indicators/term-premia-tabs",
     "source": "Federal Reserve Bank of New York ACM model",
     "frequency": "daily published model estimates", "units": "percent"},
]


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_fred():
    with zipfile.ZipFile(RAW / "rates.csv") as archive:
        frame = pd.read_csv(io.BytesIO(archive.read("daily.csv")), parse_dates=["observation_date"])
    return frame.set_index("observation_date").apply(pd.to_numeric, errors="coerce")


def load_acm():
    if not SOFFICE.exists():
        raise RuntimeError(f"Required spreadsheet converter missing: {SOFFICE}")
    with tempfile.TemporaryDirectory(prefix="case002_acm_") as tmp:
        subprocess.run(
            [str(SOFFICE), "--headless", "--convert-to", "xlsx", "--outdir", tmp,
             str(RAW / "ACMTermPremium.xls")], check=True, capture_output=True, text=True
        )
        converted = Path(tmp) / "ACMTermPremium.xlsx"
        acm = pd.read_excel(converted, sheet_name="ACM Daily", usecols=["DATE", "ACMTP10"])
    acm["DATE"] = pd.to_datetime(acm["DATE"], format="%d-%b-%Y")
    return acm.set_index("DATE")


def ols_metrics(y, x):
    correlation = float(np.corrcoef(y, x)[0, 1])
    design = np.column_stack([np.ones(len(x)), x])
    intercept, coefficient = np.linalg.lstsq(design, y, rcond=None)[0]
    fitted = intercept + coefficient * x
    sse = float(np.square(y - fitted).sum())
    sst = float(np.square(y - y.mean()).sum())
    return correlation, float(1 - sse / sst), float(coefficient), float(intercept)


def main():
    assert sha256(SPEC) == SPEC_SHA256, "Frozen specification changed; stop before calculation."
    fred = load_fred()
    acm = load_acm()
    levels = fred.join(acm, how="outer")[SERIES].loc[START:END]
    common = levels.dropna(how="any").sort_index()
    assert common.index.is_unique and common.index.is_monotonic_increasing
    assert common.index[0] == START and common.index[-1] == END

    changes = common.diff().iloc[1:] * 100.0
    transformed = common.iloc[1:].copy()
    transformed.insert(0, "prior_common_date", common.index[:-1].strftime("%Y-%m-%d"))
    transformed.insert(1, "interval_calendar_days", np.diff(common.index.values).astype("timedelta64[D]").astype(int))
    for column in SERIES:
        transformed[f"d_{column}_bp"] = changes[column].values
    transformed.index.name = "date"
    transformed.reset_index().to_csv(ROOT / "common_sample_changes.csv", index=False, float_format="%.10f")

    y = changes["DGS10"].to_numpy()
    rows = []
    for hypothesis, mechanism, column in REGRESSORS:
        x = transformed[column].to_numpy()
        correlation, r_squared, coefficient, intercept = ols_metrics(y, x)
        rows.append({
            "hypothesis": hypothesis, "mechanism": mechanism, "regressor": column,
            "correlation_with_d_DGS10": correlation, "ols_r_squared": r_squared,
            "coefficient": coefficient, "coefficient_sign": "positive" if coefficient > 0 else "non_positive",
            "matches_prespecified_positive_sign": bool(coefficient > 0), "intercept_bp": intercept,
            "N": len(y),
        })
    metrics = pd.DataFrame(rows)
    metrics.to_csv(ROOT / "first_pass_metrics.csv", index=False, float_format="%.10f")

    identity = changes["DGS10"] - changes["DFII10"] - changes["T10YIE"]
    gap_counts = transformed["interval_calendar_days"].value_counts().sort_index()
    audit = {
        "specification_sha256_before_calculation": SPEC_SHA256,
        "status": "passed",
        "calendar_boundary": {"start": str(START.date()), "end": str(END.date())},
        "common_level_first_date": str(common.index[0].date()),
        "common_level_last_date": str(common.index[-1].date()),
        "common_level_count": int(len(common)),
        "change_first_date": str(changes.index[0].date()),
        "change_last_date": str(changes.index[-1].date()),
        "identical_N_all_hypotheses": int(len(changes)),
        "all_metric_N_identical": bool(metrics.N.nunique() == 1),
        "missing_method": "strict common-date intersection; no interpolation; no forward-fill; no missing=0",
        "difference_method": "100 * current percent level minus prior common-date percent level",
        "timing": "same source-labeled date; no lags",
        "max_abs_nominal_minus_real_minus_breakeven_change_bp": float(identity.abs().max()),
        "identity_tolerance_bp": 1e-9,
        "identity_check_passed": bool(identity.abs().max() <= 1e-9),
        "interval_calendar_days_counts": {str(int(k)): int(v) for k, v in gap_counts.items()},
        "max_interval_calendar_days": int(transformed.interval_calendar_days.max()),
        "python": platform.python_version(), "pandas": pd.__version__, "numpy": np.__version__,
    }
    assert audit["all_metric_N_identical"] and audit["identity_check_passed"]
    (ROOT / "validation.json").write_text(json.dumps(audit, indent=2) + "\n")

    manifest = []
    for item in SOURCES:
        raw_path = ROOT / item["file"]
        record = dict(item)
        record.update({
            "bytes": raw_path.stat().st_size, "sha256": sha256(raw_path),
            "raw_file_mtime_utc": datetime.fromtimestamp(raw_path.stat().st_mtime, timezone.utc).isoformat(),
            "timestamp_note": "mtime records the preserved local snapshot time, not an asserted source release time",
        })
        manifest.append(record)
    (ROOT / "source_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(metrics.to_string(index=False))
    print(json.dumps(audit, indent=2))


if __name__ == "__main__":
    main()
