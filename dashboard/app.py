from pathlib import Path
import pandas as pd, streamlit as st
st.title("Retail Demand Forecasting")
p=Path("data/raw/train.csv")
if not p.exists(): st.info("Download Rossmann train.csv from Kaggle and put it in data/raw/."); st.stop()
df=pd.read_csv(p,parse_dates=["Date"])
store=st.sidebar.selectbox("Store",sorted(df.Store.unique()))
view=df[df.Store==store].sort_values("Date")
a,b=st.columns(2); a.metric("Total sales",f"{view.Sales.sum():,.0f}"); b.metric("Daily average",f"{view.Sales.mean():,.0f}")
st.line_chart(view.set_index("Date").Sales)
st.bar_chart(view.groupby("Promo").Sales.mean())
