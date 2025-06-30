from flask import Flask, render_template, request
import pandas as pd
import yfinance as yf

app = Flask(__name__)

def fetch_data(tickers):
    data = {}
    for ticker in tickers:
        data[ticker] = yf.download(ticker)
    return data

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    ticker = request.form['ticker']
    data = fetch_data([ticker])
    # Assume we have a function train_model defined elsewhere
    model = train_model(data[ticker])
    predictions = model.forecast(steps=30)
    return render_template('result.html', predictions=predictions)

if __name__ == "__main__":
    app.run(debug=True)