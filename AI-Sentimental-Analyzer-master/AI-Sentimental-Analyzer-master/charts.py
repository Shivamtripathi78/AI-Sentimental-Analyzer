import matplotlib
import matplotlib.pyplot as plt

from database import collection

def create_sentiment_chart():
    positive = collection.count_documents({"sentiment": "Positive"})
    negative = collection.count_documents({"sentiment": "Negative"})
    neutral = collection.count_documents({"sentiment": "Neutral"})

    labels = ["Positive", "Negative", "Neutral"]
    values = [positive, negative, neutral]

    plt.figure(figsize=(6, 6))
    plt.pie(values, labels=labels, autopct="%1.1f%%")
    plt.title("Sentiment Analysis")

    plt.savefig("static/charts/sentiment_chart.png")
    plt.close()