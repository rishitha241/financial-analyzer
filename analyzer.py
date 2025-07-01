import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    return pd.read_csv(file_path)

def moving_average(data, window=5):
    return data['Close'].rolling(window=window).mean()

def plot_data(data):
    plt.figure(figsize=(10, 5))
    plt.plot(data['Date'], data['Close'], label='Close Price')
    plt.plot(data['Date'], moving_average(data), label='5-Day MA', linestyle='--')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.title('Stock Price Trend')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    file_path = input("Enter path to stock data CSV file: ")
    data = load_data(file_path)
    plot_data(data)
