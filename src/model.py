from pathlib import Path
import json, joblib, numpy as np, pandas as pd
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
from src.features import build_features, feature_columns
def train_model(train_csv="data/raw/train.csv",store_csv="data/raw/store.csv"):
    df=pd.read_csv(train_csv,parse_dates=["Date"]).merge(pd.read_csv(store_csv),on="Store",how="left")
    df=build_features(df); cutoff=df.Date.max()-pd.Timedelta(days=42)
    cols=feature_columns(df); data=df.dropna(subset=cols+["Sales"])
    tr=data[data.Date<=cutoff]; va=data[data.Date>cutoff]
    if tr.empty or va.empty: raise ValueError("Insufficient rows for chronological validation.")
    model=ExtraTreesRegressor(n_estimators=200,min_samples_leaf=2,random_state=42,n_jobs=-1)
    model.fit(tr[cols],tr.Sales); pred=np.maximum(0,model.predict(va[cols]))
    metrics={"mae":float(mean_absolute_error(va.Sales,pred)),"rmse":float(np.sqrt(mean_squared_error(va.Sales,pred))),
             "wape":float(np.abs(va.Sales-pred).sum()/np.abs(va.Sales).sum())}
    Path("artifacts").mkdir(exist_ok=True)
    joblib.dump({"model":model,"features":cols},"artifacts/sales_model.joblib")
    Path("artifacts/metrics.json").write_text(json.dumps(metrics,indent=2))
    return metrics
def load_model(): return joblib.load("artifacts/sales_model.joblib")
