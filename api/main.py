from pathlib import Path
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import pandas as pd
from src.model import load_artifact

app = FastAPI(title="Retail Demand Forecasting API", version="1.0.0")

class ForecastRequest(BaseModel):
    store: int = Field(gt=0)
    date: str
    day_of_week: int = Field(ge=1, le=7)
    promo: int = Field(ge=0, le=1)
    state_holiday: str = "0"
    school_holiday: int = Field(ge=0, le=1)
    year: int
    month: int = Field(ge=1, le=12)
    day: int = Field(ge=1, le=31)
    week_of_year: int = Field(ge=1, le=53)
    sales_lag_1: float = Field(ge=0)
    sales_lag_7: float = Field(ge=0)
    sales_lag_14: float = Field(ge=0)
    sales_lag_28: float = Field(ge=0)
    sales_roll_mean_7: float = Field(ge=0)
    sales_roll_mean_28: float = Field(ge=0)

@app.get("/health")
def health():
    return {"status": "ok", "model_available": Path("artifacts/sales_model.joblib").exists()}

@app.post("/forecast")
def forecast(request: ForecastRequest):
    try:
        artifact = load_artifact()
    except FileNotFoundError:
        raise HTTPException(status_code=503, detail="Train the model first: python -m src.pipeline")
    payload = request.model_dump()
    payload.pop("date")
    row = pd.DataFrame([{name: payload[name] for name in artifact["features"]}])
    prediction = max(0.0, float(artifact["model"].predict(row)[0]))
    return {"store": request.store, "date": request.date, "predicted_sales": round(prediction, 2)}
