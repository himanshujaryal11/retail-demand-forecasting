import pandas as pd
from src.features import build_features

def test_feature_engineering_creates_calendar_and_lags():
    df = pd.DataFrame({
        "Store": [1] * 35,
        "Date": pd.date_range("2024-01-01", periods=35),
        "Sales": list(range(35)),
        "DayOfWeek": [1] * 35,
        "Promo": [0] * 35,
        "StateHoliday": ["0"] * 35,
        "SchoolHoliday": [0] * 35,
    })
    result = build_features(df)
    assert "Year" in result
    assert "Sales_lag_7" in result
    assert result.loc[7, "Sales_lag_7"] == 0
