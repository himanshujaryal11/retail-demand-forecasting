from pathlib import Path
import json
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Retail Demand Forecasting", layout="wide")
st.title("Retail Demand Forecasting")
st.caption("Store-level sales analysis using the Rossmann Store Sales dataset.")

data_path = Path("data/raw/train.csv")
if not data_path.exists():
    st.info("Download train.csv from the Kaggle Rossmann Store Sales competition and place it in data/raw/.")
    st.stop()

df = pd.read_csv(data_path, parse_dates=["Date"])
st.sidebar.header("Filters")
stores = sorted(df["Store"].dropna().unique().tolist())
selected = st.sidebar.selectbox("Store", stores)
store_df = df[df["Store"] == selected].sort_values("Date")
c1, c2, c3 = st.columns(3)
c1.metric("Total sales", f"{store_df['Sales'].sum():,.0f}")
c2.metric("Average daily sales", f"{store_df['Sales'].mean():,.0f}")
c3.metric("Observed days", f"{len(store_df):,}")
st.subheader("Daily sales")
st.line_chart(store_df.set_index("Date")["Sales"])
st.subheader("Promotion comparison")
if "Promo" in store_df:
    st.bar_chart(store_df.groupby("Promo")["Sales"].mean())
metrics_path = Path("artifacts/metrics.json")
if metrics_path.exists():
    st.subheader("Latest validation metrics")
    st.json(json.loads(metrics_path.read_text()))
else:
    st.caption("Validation metrics appear here after the training pipeline has been run.")
