from __future__ import annotations
import pandas as pd

TARGET = "Sales"
BASE_FEATURES = [
    "Store", "DayOfWeek", "Promo", "StateHoliday", "SchoolHoliday",
    "Year", "Month", "Day", "WeekOfYear",
]

def build_features(frame: pd.DataFrame) -> pd.DataFrame:
    """Create calendar and within-store lag features from daily observations."""
    df = frame.copy()
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values(["Store", "Date"]).reset_index(drop=True)
    df["Year"] = df["Date"].dt.year
    df["Month"] = df["Date"].dt.month
    df["Day"] = df["Date"].dt.day
    df["WeekOfYear"] = df["Date"].dt.isocalendar().week.astype(int)
    for lag in (1, 7, 14, 28):
        df[f"Sales_lag_{lag}"] = df.groupby("Store")[TARGET].shift(lag)
    for window in (7, 28):
        df[f"Sales_roll_mean_{window}"] = (
            df.groupby("Store")[TARGET].transform(
                lambda s: s.shift(1).rolling(window, min_periods=window).mean()
            )
        )
    return df

def feature_columns(frame: pd.DataFrame) -> list[str]:
    cols = BASE_FEATURES + [
        c for c in frame.columns
        if c.startswith("Sales_lag_") or c.startswith("Sales_roll_mean_")
    ]
    return [c for c in cols if c in frame.columns]
