# Retail Demand Forecasting and Store Analytics

A practical store-level retail analytics project using the Rossmann Store Sales dataset. It explores daily sales, promotion and calendar effects, builds a leakage-aware forecasting baseline, and exposes predictions through an API and dashboard.

## Dataset
Download `train.csv` and `store.csv` from the [Kaggle Rossmann Store Sales competition](https://www.kaggle.com/competitions/rossmann-store-sales/data). Put them in `data/raw/`. The dataset is not redistributed here; follow Kaggle's competition terms.

## Implemented project components
- Python data preparation, calendar/lag/rolling features and chronological validation.
- Extra Trees regression baseline and MAE, RMSE and WAPE metrics.
- MySQL schema and example analytical SQL.
- FastAPI prediction endpoint and Streamlit exploratory dashboard.
- Promotion comparison for planning support.
- Optional VADER review sentiment module for a separate reviews CSV.

## Stack
Python, Pandas, NumPy, scikit-learn, MySQL, SQL, Matplotlib, Seaborn, Plotly, FastAPI, Streamlit, NLTK/VADER, Docker, pytest and GitHub Actions.

## Setup
```bash
python -m venv .venv
# Windows PowerShell: .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```
Put the two Kaggle CSV files under `data/raw/`, then run:
```bash
python -m src.pipeline
pytest
uvicorn api.main:app --reload
streamlit run dashboard/app.py
``

## Notes on scope and validity
Rossmann is store-level, not SKU-level, so product-level collaborative recommendations are not supported by this dataset. Review sentiment requires an independent `reviews.csv` with a `review` column. Forecast quality must be evaluated after downloading and running the data; no performance result is claimed in advance. For future multi-day forecasts, lag features must be updated using observed sales or a recursive strategy. Reorder quantities additionally need lead-time, stock-on-hand and service-level inputs.

Code is MIT licensed. Dataset terms are set by Kaggle and are separate from this repository.
