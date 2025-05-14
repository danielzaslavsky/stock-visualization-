import os
from datetime import datetime
import pandas as pd
import yfinance as yf
import plotly.graph_objs as go

# Create necessary directories
os.makedirs("data", exist_ok=True)
os.makedirs("plots", exist_ok=True)


def fetch_stock_data(ticker: str, start: str, end: str) -> pd.DataFrame:
    """
    Fetch historical stock data from Yahoo Finance.

    Parameters:
        ticker (str): Stock ticker symbol.
        start (str): Start date in YYYY-MM-DD format.
        end (str): End date in YYYY-MM-DD format.

    Returns:
        pd.DataFrame: DataFrame containing historical stock prices.
    """
    try:
        stock_data = yf.download(ticker, start=start, end=end)
        if stock_data.empty:
            print("No data found for the given ticker and date range.")
        return stock_data
    except Exception as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame()


def plot_stock_data(df: pd.DataFrame, ticker: str) -> None:
    """
    Plot closing prices of the stock using Plotly and save the plot.

    Parameters:
        df (pd.DataFrame): DataFrame with stock data.
        ticker (str): Ticker symbol used in the title.
    """
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df['Close'], mode='lines', name='Close Price'))
    fig.update_layout(title=f"{ticker.upper()} Closing Price Over Time",
                      xaxis_title="Date",
                      yaxis_title="Closing Price (USD)",
                      template="plotly_dark")

    fig.write_html(f"plots/{ticker}_plot.html")
    print(f"Plot saved to plots/{ticker}_plot.html")
    fig.show()


def save_data(df: pd.DataFrame, ticker: str, start: str, end: str) -> None:
    """
    Save stock data to CSV file.

    Parameters:
        df (pd.DataFrame): Stock data to save.
        ticker (str): Stock ticker symbol.
        start (str): Start date.
        end (str): End date.
    """
    filename = f"data/{ticker}_{start}_{end}.csv"
    df.to_csv(filename)
    print(f"Data saved to {filename}")


def main():
    print("Welcome to the Stock Visualization Tool")
    ticker = input("Enter stock ticker (e.g., AAPL): ").strip().upper()
    start_date = input("Enter start date (YYYY-MM-DD): ").strip()
    end_date = input("Enter end date (YYYY-MM-DD): ").strip()

    try:
        datetime.strptime(start_date, "%Y-%m-%d")
        datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    df = fetch_stock_data(ticker, start_date, end_date)
    if not df.empty:
        save_data(df, ticker, start_date, end_date)
        plot_stock_data(df, ticker)


if __name__ == "__main__":
    main()
