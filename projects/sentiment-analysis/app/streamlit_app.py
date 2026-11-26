"""Simple Streamlit interface for the trained sentiment baseline."""
from pathlib import Path
import joblib
import streamlit as st

MODEL_PATH = Path(__file__).resolve().parents[1] / "models" / "sentiment_baseline.joblib"

st.set_page_config(page_title="Social Media Sentiment Analysis", page_icon="💬")
st.title("Social Media Sentiment Analysis")
st.write("Enter a post or comment to predict its sentiment.")

if not MODEL_PATH.exists():
    st.warning("Train the baseline first by running: python src/train_baseline.py")
else:
    model = joblib.load(MODEL_PATH)
    message = st.text_area("Social media post", placeholder="I really enjoyed this product!")
    if st.button("Analyse sentiment", type="primary"):
        if message.strip():
            prediction = model.predict([message])[0]
            st.subheader(f"Predicted sentiment: {prediction}")
            if hasattr(model, "predict_proba"):
                probabilities = model.predict_proba([message])[0]
                st.bar_chart(dict(zip(model.classes_, probabilities)))
        else:
            st.info("Please enter some text.")
