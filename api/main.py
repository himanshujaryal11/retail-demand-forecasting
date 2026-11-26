from pathlib import Path
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
import pandas as pd
from src.model import load_model
app=FastAPI(title="Retail Demand Forecasting API")
class ForecastInput(BaseModel):
    Store:int; DayOfWeek:int; Promo:int; StateHoliday:str="0"; SchoolHoliday:int=0
    Year:int; Month:int; Day:int; WeekOfYear:int
    Sales_lag_1:float; Sales_lag_7:float; Sales_lag_14:float; Sales_lag_28:float
    Sales_roll_mean_7:float; Sales_roll_mean_28:float
@app.get("/health")
def health(): return {"status":"ok","model_available":Path("artifacts/sales_model.joblib").exists()}
@app.post("/forecast")
def forecast(x:ForecastInput):
    try: obj=load_model()
    except FileNotFoundError: raise HTTPException(503,"Run python -m src.pipeline first.")
    row=pd.DataFrame([x.model_dump()])[obj["features"]]
    return {"predicted_sales":round(max(0,float(obj["model"].predict(row)[0])),2)}
