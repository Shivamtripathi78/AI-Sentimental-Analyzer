from transformers import pipeline

classifier = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

def analyze_sentiment(text):
    result = classifier(text)[0]

    sentiment = result["label"]
    score = round(result["score"] * 100, 2)

    return sentiment, score