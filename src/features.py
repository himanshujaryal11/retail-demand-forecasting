import pandas as pd
TARGET = "Sales"
BASE_FEATURES = ["Store","DayOfWeek","Promo","StateHoliday","SchoolHoliday","Year","Month","Day","WeekOfYear"]
def build_features(frame):
    df=frame.copy()
    df["Date"]=pd.to_datetime(df["Date"])
    df=df.sort_values(["Store","Date"]).reset_index(drop=True)
    df["Year"]=df.Date.dt.year; df["Month"]=df.Date.dt.month
    df["Day"]=df.Date.dt.day; df["WeekOfYear"]=df.Date.dt.isocalendar().week.astype(int)
    for lag in (1,7,14,28): df[f"Sales_lag_{lag}"]=df.groupby("Store").Sales.shift(lag)
    for w in (7,28):
        df[f"Sales_roll_mean_{w}"]=df.groupby("Store").Sales.transform(lambda s:s.shift(1).rolling(w,min_periods=w).mean())
    return df
def feature_columns(df):
    cols=BASE_FEATURES+[c for c in df if c.startswith("Sales_lag_") or c.startswith("Sales_roll_mean_")]
    return [c for c in cols if c in df]
