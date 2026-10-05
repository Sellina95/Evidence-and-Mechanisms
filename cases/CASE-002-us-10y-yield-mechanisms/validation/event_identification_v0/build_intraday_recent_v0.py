from pathlib import Path
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import csv
import json

import yfinance as yf

BASE = Path(
    "cases/CASE-002-us-10y-yield-mechanisms/"
    "validation/event_identification_v0"
)

EVENTS = BASE / "events.csv"
OUT = BASE / "intraday_recent_v0.csv"
MANIFEST = BASE / "intraday_recent_manifest_v0.json"

TICKERS = ["SHY", "IEF", "TLT", "TIP"]
ET = ZoneInfo("America/New_York")

# --------------------------------------------------
# 1. Download recent 5-minute ETF data
# Yahoo/yfinance intraday availability is limited.
# We intentionally use only what is actually returned.
# --------------------------------------------------

data = {}
coverage = {}

for ticker in TICKERS:
    print("Downloading", ticker)

    df = yf.Ticker(ticker).history(
        period="60d",
        interval="5m",
        prepost=True,
        auto_adjust=False,
        actions=False,
    )

    if df.empty:
        print("  NO DATA")
        data[ticker] = df
        coverage[ticker] = None
        continue

    # Normalize timezone to US Eastern.
    if df.index.tz is None:
        df.index = df.index.tz_localize(ET)
    else:
        df.index = df.index.tz_convert(ET)

    df = df.sort_index()
    data[ticker] = df

    coverage[ticker] = {
        "first": df.index[0].isoformat(),
        "last": df.index[-1].isoformat(),
        "rows": len(df),
    }

    print(
        " ",
        df.index[0],
        "->",
        df.index[-1],
        "rows",
        len(df),
    )


def closest_close(df, target, tolerance_minutes=8):
    """
    Return the closest available Close observation to target,
    but only if it is within the fixed tolerance.
    """
    if df.empty:
        return None, None

    differences = abs(df.index - target)
    pos = differences.argmin()

    ts = df.index[pos]

    if abs((ts - target).total_seconds()) > tolerance_minutes * 60:
        return None, None

    val = df.iloc[pos]["Close"]

    try:
        return ts, float(val)
    except Exception:
        return None, None


def pct_return(start_px, end_px):
    if start_px is None or end_px is None or start_px == 0:
        return None
    return (end_px / start_px - 1.0) * 100.0


# --------------------------------------------------
# 2. Load event calendar
# --------------------------------------------------

with EVENTS.open(newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    fields = list(reader.fieldnames)

out_rows = []

covered_events = 0
uncovered_events = 0

for r in rows:

    # Known market-closed event; do not substitute.
    if "MARKET_CLOSED_GOOD_FRIDAY" in r.get("notes", ""):
        continue

    event_dt = datetime.strptime(
        r["event_date"] + " " + r["event_time_et"],
        "%Y-%m-%d %H:%M",
    ).replace(tzinfo=ET)

    # Frozen window:
    # FOMC press conference: T-5m -> T+30m
    # All other events:      T-10m -> T+30m
    # Robustness:            same start -> T+60m
    pre_minutes = (
        5
        if r["event_type"] == "FOMC_PRESS_CONFERENCE"
        else 10
    )

    start_dt = event_dt - timedelta(minutes=pre_minutes)
    end30_dt = event_dt + timedelta(minutes=30)
    end60_dt = event_dt + timedelta(minutes=60)

    result = {
        "event_id": r["event_id"],
        "event_type": r["event_type"],
        "event_date": r["event_date"],
        "event_time_et": r["event_time_et"],
        "window_start_et": start_dt.strftime("%Y-%m-%d %H:%M"),
        "window_end30_et": end30_dt.strftime("%Y-%m-%d %H:%M"),
        "window_end60_et": end60_dt.strftime("%Y-%m-%d %H:%M"),
    }

    event_has_any = False

    for ticker in TICKERS:
        df = data[ticker]

        t0, p0 = closest_close(df, start_dt)
        t30, p30 = closest_close(df, end30_dt)
        t60, p60 = closest_close(df, end60_dt)

        ret30 = pct_return(p0, p30)
        ret60 = pct_return(p0, p60)

        key = ticker.lower()

        result[f"{key}_start_bar_et"] = (
            t0.strftime("%Y-%m-%d %H:%M") if t0 else ""
        )
        result[f"{key}_end30_bar_et"] = (
            t30.strftime("%Y-%m-%d %H:%M") if t30 else ""
        )
        result[f"{key}_end60_bar_et"] = (
            t60.strftime("%Y-%m-%d %H:%M") if t60 else ""
        )
        result[f"{key}_ret30_pct"] = (
            f"{ret30:.6f}" if ret30 is not None else ""
        )
        result[f"{key}_ret60_pct"] = (
            f"{ret60:.6f}" if ret60 is not None else ""
        )

        if ret30 is not None:
            event_has_any = True

    if event_has_any:
        result["status"] = "AVAILABLE"
        covered_events += 1
    else:
        result["status"] = "OUTSIDE_OR_MISSING_INTRADAY_COVERAGE"
        uncovered_events += 1

    out_rows.append(result)


# --------------------------------------------------
# 3. Save raw intraday validation artifact
# --------------------------------------------------

out_fields = [
    "event_id",
    "event_type",
    "event_date",
    "event_time_et",
    "window_start_et",
    "window_end30_et",
    "window_end60_et",
]

for ticker in TICKERS:
    key = ticker.lower()
    out_fields += [
        f"{key}_start_bar_et",
        f"{key}_end30_bar_et",
        f"{key}_end60_bar_et",
        f"{key}_ret30_pct",
        f"{key}_ret60_pct",
    ]

out_fields.append("status")

with OUT.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=out_fields)
    writer.writeheader()
    writer.writerows(out_rows)


# --------------------------------------------------
# 4. Populate existing event table main-window fields
#    ONLY when recent intraday data are available.
# --------------------------------------------------

by_id = {
    r["event_id"]: r
    for r in out_rows
    if r["status"] == "AVAILABLE"
}

for r in rows:
    x = by_id.get(r["event_id"])
    if not x:
        continue

    r["intraday_shy"] = x["shy_ret30_pct"]
    r["intraday_ief"] = x["ief_ret30_pct"]
    r["intraday_tlt"] = x["tlt_ret30_pct"]
    r["intraday_tip"] = x["tip_ret30_pct"]

with EVENTS.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)


# --------------------------------------------------
# 5. Manifest
# --------------------------------------------------

manifest = {
    "contract": "CASE002_INTRADAY_RECENT_V0",
    "provider": "Yahoo Finance via yfinance",
    "interval": "5m",
    "period_requested": "60d",
    "prepost": True,
    "tickers": TICKERS,
    "main_window": {
        "FOMC_PRESS_CONFERENCE": "T-5m to T+30m",
        "OTHER_EVENTS": "T-10m to T+30m",
    },
    "robustness_window": "same start to T+60m",
    "interpretation": (
        "ETF price responses are confirmation proxies only; "
        "they are not direct Treasury-yield observations."
    ),
    "coverage": coverage,
    "events_available": covered_events,
    "events_unavailable": uncovered_events,
}

MANIFEST.write_text(
    json.dumps(manifest, indent=2),
    encoding="utf-8",
)

print("\nINTRADAY BUILD COMPLETE")
print("AVAILABLE EVENTS:", covered_events)
print("UNAVAILABLE EVENTS:", uncovered_events)
print("WROTE:", OUT)
print("WROTE:", MANIFEST)
