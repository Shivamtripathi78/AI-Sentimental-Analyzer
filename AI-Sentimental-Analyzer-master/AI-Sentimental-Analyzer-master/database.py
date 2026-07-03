import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["sentimentDB"]

reviews = db["reviews"]



def generate_chart():
    positive = reviews.count_documents({"sentiment": "positive"})
    negative = reviews.count_documents({"sentiment": "negative"})
    neutral = reviews.count_documents({"sentiment": "neutral"})
    print("Positive:" ,positive)
    print("Negative:" ,negative)
    print("Neutral:" ,neutral)

    sizes = [positive, negative, neutral]

    if sum(sizes) == 0:
        print("No data available for chart")
        return

    import matplotlib.pyplot as plt

    plt.figure(figsize=(6,6))
    plt.pie(
        sizes,
        labels=["Positive", "Negative", "Neutral"],
        autopct="%1.1f%%"
    )

    plt.savefig("static/charts/sentiment_chart.png")
    plt.close()