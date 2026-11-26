from __future__ import annotations
from pathlib import Path
import json
import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
from src.features import build_features, feature_columns, TARGET

def wape(y_true, y_pred) -> float:
    denom = np.abs(np.asarray(y_true)).sum()
    return float(np.abs(np.asarray(y_true) - np.asarray(y_pred)).sum() / denom) if denom else float("nan")

def train_model(train_csv: str = "data/raw/train.csv", store_csv: str = "data/raw/store.csv",
                artifact_dir: str = "artifacts") -> dict:
    sales = pd.read_csv(train_csv, parse_dates=["Date"])
    stores = pd.read_csv(store_csv)
    df = sales.merge(stores, on="Store", how="left")
    df = build_features(df)
    # Use the latest 6 weeks as a chronological validation window.
    cutoff = df["Date"].max() - pd.Timedelta(days=42)
    features = feature_columns(df)
    usable = df.dropna(subset=features + [TARGET]).copy()
    tr = usable[usable["Date"] <= cutoff]
    va = usable[usable["Date"] > cutoff]
    if tr.empty or va.empty:
        raise ValueError("Not enough history for a 42-day chronological validation split.")
    model = ExtraTreesRegressor(n_estimators=250, min_samples_leaf=2,
                                random_state=42, n_jobs=-1)
    model.fit(tr[features], tr[TARGET])
    pred = np.maximum(0, model.predict(va[features]))
    metrics = {
        "validation_start": str(va["Date"].min().date()),
        "validation_end": str(va["Date"].max().date()),
        "rows_train": int(len(tr)),
        "rows_validation": int(len(va)),
        "mae": float(mean_absolute_error(va[TARGET], pred)),
        "rmse": float(np.sqrt(mean_squared_error(va[TARGET], pred))),
        "wape": wape(va[TARGET], pred),
    }
    out = Path(artifact_dir)
    out.mkdir(parents=True, exist_ok=True)
    joblib.dump({"model": model, "features": features}, out / "sales_model.joblib")
    (out / "metrics.json").write_text(json.dumps(metrics, indent=2))
    return metrics

def load_artifact(path: str = "artifacts/sales_model.joblib"):
    return joblib.load(path)
