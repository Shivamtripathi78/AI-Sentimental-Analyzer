from flask import Flask, request, jsonify, render_template
import pandas as pd

from model import analyze_sentiment
from database import reviews
from database import generate_chart

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/analyze', methods=['POST'])
def analyze():

    data = request.json
    text = data["text"]

    sentiment, score = analyze_sentiment(text)

    reviews.insert_one({
        "text": text,
        "sentiment": sentiment,
        "score": score
    })

    generate_chart()

    return jsonify({
        "sentiment": sentiment,
        "score": score
    })


@app.route('/history')
def history():
    data = list(reviews.find({}, {"_id": 0}))
    return jsonify(data)


@app.route('/upload_csv', methods=['POST'])
def upload_csv():

    file = request.files['file']

    df = pd.read_csv(file)

    for review in df['review']:

        sentiment, score = analyze_sentiment(review)

        reviews.insert_one({
            "text": review,
            "sentiment": sentiment,
            "score": score
        })

    generate_chart()

    return "CSV Uploaded Successfully!"


if __name__ == "__main__":
    app.run(debug=True)