from __future__ import annotations
import pandas as pd

def analyse_reviews(csv_path: str = "data/raw/reviews.csv") -> pd.DataFrame:
    """Optional VADER sentiment analysis for an external reviews.csv file.

    Expected input column: review. Reviews are not supplied by the Rossmann dataset.
    """
    try:
        from nltk.sentiment import SentimentIntensityAnalyzer
        import nltk
    except ImportError as exc:
        raise RuntimeError("Install nltk to use optional review analysis.") from exc
    try:
        sia = SentimentIntensityAnalyzer()
    except LookupError:
        nltk.download("vader_lexicon", quiet=True)
        sia = SentimentIntensityAnalyzer()
    reviews = pd.read_csv(csv_path)
    if "review" not in reviews:
        raise ValueError("reviews.csv must contain a 'review' column.")
    reviews["sentiment_score"] = reviews["review"].fillna("").astype(str).map(
        lambda text: sia.polarity_scores(text)["compound"]
    )
    reviews["sentiment"] = reviews["sentiment_score"].map(
        lambda score: "positive" if score >= 0.05 else ("negative" if score <= -0.05 else "neutral")
    )
    return reviews
