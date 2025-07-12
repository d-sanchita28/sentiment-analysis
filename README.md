# Aspect-Based Sentiment Analysis for Product Reviews

## Overview
This project performs aspect-based sentiment analysis on product reviews using SpaCy, FastText, and machine learning classifiers. It extracts product features (aspects) from reviews and classifies sentiment (positive/negative) for each aspect.

## Features
- Aspect extraction from review text
- Sentiment classification for each aspect
- REST API for inference

## Setup

```sh
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

## Training

```sh
python prepare_fasttext_data.py   # Prepares fasttext_data.txt from all CSVs
python ft.py         # Trains or loads FastText embeddings
python training.py   # Trains or loads the main classifier
```

## Running the API

```sh
python server.py
```
The API will be available at `http://localhost:5000/`.

## Example API Usage

Send a POST request to `/` with the form field `filename` (the name of a CSV file in `csv_files/`):

```sh
curl -X POST -F "filename=yourfile.csv" http://localhost:5000/
```

## Sample Output

```json
[
  {
    "category": "camera",
    "sentence": "camera is very very poor.",
    "sentiment": "Negative"
  },
  ...
]
```

## Accuracy and Classification Report

```
fit_time :      0.033713 (+/- 0.081872)
score_time :    0.008344 (+/- 0.010503)
test_accuracy : 0.638095 (+/- 0.097124)
test_precision_macro :  0.679584 (+/- 0.245189)
test_recall_macro :     0.579808 (+/- 0.107514)
Classification Report on Training Set:
              precision    recall  f1-score   support
    Negative       1.00      0.86      0.93        44
    Positive       0.91      1.00      0.95        61
    accuracy                           0.94       105
   macro avg       0.96      0.93      0.94       105
weighted avg       0.95      0.94      0.94       105
```

## Folder Structure

- `csv_files/` — Input review CSVs
- `models/` — Saved models (not tracked in git)
- `*.py` — Source code

---

