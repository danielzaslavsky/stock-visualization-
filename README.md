# 📈 Stock Visualization Tool

Welcome to the Stock Visualization Tool – a Python-based application that allows users to fetch historical stock price data and generate interactive visualizations using Plotly. This tool is ideal for finance enthusiasts, data science learners, and anyone interested in analyzing stock market trends.

---

## 🚀 Features

- Fetch historical stock data via Yahoo Finance
- Plot closing prices as interactive line graphs
- Save plots as standalone HTML files for sharing or analysis
- Automatically store fetched data as CSV files
- Easy-to-use command-line interface
- Clean, modular codebase ideal for learning and extension

---

## 🛠 Installation

1. Clone the repository.
2. (Optional) Create and activate a virtual environment.
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the tool from the command line:
   ```bash
   python main.py TICKER --start YYYY-MM-DD --end YYYY-MM-DD
   ```
   If you omit the arguments you will be prompted for them interactively.

If run without command-line arguments you will be prompted for:

- A stock ticker symbol (e.g., `AAPL`)
- A start date (e.g., `2020-01-01`)
- An end date (e.g., `2023-12-31`)

After gathering the information, the script will:

- Fetch the data
- Save it as a CSV in the `data/` folder
- Generate an interactive plot and save it to the `plots/` folder
