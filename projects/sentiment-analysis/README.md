# Sentiment Analysis of Social Media Posts

An NLP project that classifies social media posts and comments as **positive**, **negative**, or **neutral**. It compares a traditional machine-learning baseline with deep-learning approaches such as LSTM and BERT.

## Objectives
- Clean and preprocess informal social-media text.
- Explore sentiment patterns and class balance.
- Build a TF-IDF + Logistic Regression baseline.
- Compare LSTM and BERT models.
- Evaluate using accuracy, precision, recall, F1-score, and a confusion matrix.
- Build an interactive Streamlit app for sentiment predictions.

## Dataset
Use a labelled CSV with at least these columns:
- `text`: social media post or comment
- `sentiment`: positive, negative, or neutral

Sentiment140 is a popular starting point for binary positive/negative classification. For a three-class project, select a dataset that explicitly includes neutral labels. Check the dataset licence and label definitions. Save the file as `data/raw/social_media_sentiment.csv`. Do not commit large datasets or private user information.

## Structure
```text
sentiment-analysis/
├── README.md
├── requirements.txt
├── data/raw/
├── models/
├── src/
│   ├── data_preprocessing.py
│   └── train_baseline.py
└── app/
    └── streamlit_app.py
```

## Setup (Windows PowerShell)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If activation is blocked in the current PowerShell session:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

## Workflow
1. Load the labelled CSV and inspect missing values, duplicates, and class balance.
2. Clean text carefully; retain negations and sentiment-bearing words.
3. Split train/test data with stratification.
4. Train TF-IDF + Logistic Regression as the baseline.
5. Evaluate with per-class precision, recall, F1-score, and a confusion matrix.
6. Compare with LSTM and BERT using the same held-out test set.
7. Deploy the selected model in the Streamlit app.

## Important
Do not claim model performance until the models have actually been trained and evaluated. Prevent data leakage by fitting text vectorizers only on training data. Record dataset source, licence, preprocessing choices, random seed, and model settings.

## Run
After implementing the training and app scripts:
```powershell
python src/train_baseline.py
streamlit run app/streamlit_app.py
``

## Technologies
Python, pandas, NumPy, scikit-learn, NLTK, TensorFlow/Keras or PyTorch, Hugging Face Transformers, and Streamlit.
