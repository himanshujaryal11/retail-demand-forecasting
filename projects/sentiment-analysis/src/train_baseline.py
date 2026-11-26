"""Train a TF-IDF + Logistic Regression sentiment baseline."""
from pathlib import Path
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from data_preprocessing import clean_text

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "raw" / "social_media_sentiment.csv"
MODEL_PATH = ROOT / "models" / "sentiment_baseline.joblib"


def main():
    if not DATA_PATH.exists():
        raise FileNotFoundError(
            f"Dataset not found: {DATA_PATH}. Add a labelled CSV with 'text' "
            "and 'sentiment' columns."
        )

    data = pd.read_csv(DATA_PATH)
    required = {"text", "sentiment"}
    if not required.issubset(data.columns):
        raise ValueError("CSV must contain 'text' and 'sentiment' columns.")

    data = data.dropna(subset=["text", "sentiment"]).copy()
    data["text"] = data["text"].map(clean_text)
    data = data[data["text"].str.len() > 0]

    X_train, X_test, y_train, y_test = train_test_split(
        data["text"], data["sentiment"], test_size=0.2,
        random_state=42, stratify=data["sentiment"]
    )

    model = Pipeline([
        ("tfidf", TfidfVectorizer(ngram_range=(1, 2), max_features=50000)),
        ("classifier", LogisticRegression(max_iter=1000, class_weight="balanced")),
    ])
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    print(classification_report(y_test, predictions, zero_division=0))
    print("Confusion matrix:")
    print(confusion_matrix(y_test, predictions))

    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    print(f"Saved model to {MODEL_PATH}")


if __name__ == "__main__":
    main()
