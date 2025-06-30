import pandas as pd
import matplotlib.pyplot as plt

def plot_price(data):
    for ticker, df in data.items():
        plt.figure(figsize=(12, 6))
        plt.plot(df['Close'], label=ticker)
        plt.title(f'{ticker} Closing Prices')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.grid(True)
        plt.show()

if __name__ == "__main__":
    # Load your data
    data = {
        'AAPL': pd.read_csv('AAPL.csv'),
        'MSFT': pd.read_csv('MSFT.csv'),
        'GOOGL': pd.read_csv('GOOGL.csv'),
    }
    plot_price(data)

    def add_features(df):
    df['MA_20'] = df['Close'].rolling(window=20).mean()
    df['MA_50'] = df['Close'].rolling(window=50).mean()
    df['Returns'] = df['Close'].pct_change()
    return df

if __name__ == "__main__":
    data = fetch_data(["AAPL", "MSFT", "GOOGL"], "2020-01-01", "2025-06-12")
    for ticker in data.keys():
        data[ticker] = add_features(data[ticker])
