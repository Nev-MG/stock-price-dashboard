import yfinance as yf

def fetch_data(tickers, start_date, end_date):
    data = {}
    for ticker in tickers:
        data[ticker] = yf.download(ticker, start=start_date, end=end_date)
    return data

if __name__ == "__main__":
    tickers = ["AAPL", "MSFT", "GOOGL"]  # Add more tickers as needed
    data = fetch_data(tickers, "2020-01-01", "2025-06-12")
    for ticker, df in data.items():
        print(f"\n{ticker} Data:")
        print(df.head())