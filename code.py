import os

# Define project structure
project_name = "stock_visualization_tool"
os.makedirs(f"{project_name}/data", exist_ok=True)
os.makedirs(f"{project_name}/plots", exist_ok=True)
os.makedirs(f"{project_name}/utils", exist_ok=True)

# main.py content
main_py = """
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

def fetch_stock_data(ticker, start, end):
    data = yf.download(ticker, start=start, end=end)
    return data

def plot_stock_data(data, ticker):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name='Close Price'))
    fig.update_layout(title=f'{ticker} Closing Prices',
                      xaxis_title='Date',
                      yaxis_title='Price (USD)')
    fig.show()

if __name__ == "__main__":
    ticker = input("Enter stock ticker (e.g., AAPL): ").upper()
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")

    stock_data = fetch_stock_data(ticker, start_date, end_date)
    if not stock_data.empty:
        plot_stock_data(stock_data, ticker)
    else:
        print("No data found for the given parameters.")
"""

# README.md content
readme_md = f"""
# Stock Visualization Tool

A simple Python tool for fetching and visualizing stock data using Yahoo Finance.

## Features
- Fetches historical stock data using `yfinance`
- Interactive time-series plots using `plotly`
- CLI interface for user input

