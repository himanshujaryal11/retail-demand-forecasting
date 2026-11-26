import pandas as pd
from src.features import build_features
def test_lag():
    x=pd.DataFrame({"Store":[1]*35,"Date":pd.date_range("2024-01-01",periods=35),"Sales":range(35)})
    y=build_features(x)
    assert y.loc[7,"Sales_lag_7"]==0
