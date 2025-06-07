import argparse
from datetime import datetime
import pandas as pd
import yfinance as yf
import plotly.graph_objs as go
import os

# Ensure output directories exist
os.makedirs("data", exist_ok=True)
os.makedirs("plots", exist_ok=True)


def fetch_stock_data(ticker: str, start: str, end: str) -> pd.DataFrame:
    """Fetch historical stock data from Yahoo Finance."""
    try:
        df = yf.download(ticker, start=start, end=end)
        if df.empty:
            print("No data found for the given ticker and date range.")
        return df
    except Exception as exc:
        print(f"Error fetching data: {exc}")
        return pd.DataFrame()


def plot_stock_data(df: pd.DataFrame, ticker: str) -> None:
    """Plot closing prices and save the result as an HTML file."""
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df["Close"], mode="lines", name="Close"))
    fig.update_layout(
        title=f"{ticker.upper()} Closing Price Over Time",
        xaxis_title="Date",
        yaxis_title="Closing Price (USD)",
        template="plotly_dark",
    )
    output_path = f"plots/{ticker}_plot.html"
    fig.write_html(output_path)
    print(f"Plot saved to {output_path}")
    fig.show()


def save_data(df: pd.DataFrame, ticker: str, start: str, end: str) -> None:
    """Save fetched data to a CSV file."""
    path = f"data/{ticker}_{start}_{end}.csv"
    df.to_csv(path)
    print(f"Data saved to {path}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fetch and plot stock data from Yahoo Finance")
    parser.add_argument("ticker", nargs="?", help="Stock ticker symbol (e.g., AAPL)")
    parser.add_argument("--start", dest="start", help="Start date YYYY-MM-DD")
    parser.add_argument("--end", dest="end", help="End date YYYY-MM-DD")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    ticker = args.ticker or input("Enter stock ticker (e.g., AAPL): ").strip().upper()
    start_date = args.start or input("Enter start date (YYYY-MM-DD): ").strip()
    end_date = args.end or input("Enter end date (YYYY-MM-DD): ").strip()

    try:
        datetime.strptime(start_date, "%Y-%m-%d")
        datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    df = fetch_stock_data(ticker, start_date, end_date)
    if df.empty:
        return
    save_data(df, ticker, start_date, end_date)
    plot_stock_data(df, ticker)


if __name__ == "__main__":
    main()
