# Stock Volatility Calculation

This Python script calculates the daily and yearly volatility of a set of stocks using historical stock price data.

## Prerequisites

Before running the script, ensure you have the following Python libraries installed:

- pandas
- numpy
- matplotlib
- pandas_datareader

You can install these libraries using pip:

```bash
pip install pandas numpy matplotlib pandas_datareader
```

## Usage

1. Data Preparation:
    - Place your stock ticker symbols in a CSV file named stocks.csv. Each symbol should be in a separate column, and the first row should contain the symbols.
    - Ensure you have historical stock price data available. The script retrieves data from Yahoo Finance using `pandas_datareader`.
      
2. Running the Script:
    - Run the Python script `stock_volatility.py`.
    - The script will calculate daily and yearly volatility for each stock using historical price data and output the results to a CSV file named volatility.csv.
  
3. Output:
    - The output CSV file `volatility.csv` contains the calculated daily and yearly volatility for each stock.
    - Each row represents a date, and each column represents a stock symbol.

## Script Overview

- Import Libraries: Import necessary Python libraries including pandas, numpy, matplotlib, and pandas_datareader.
- Read Stock Tickers: Read stock ticker symbols from `stocks.csv`.
- Retrieve Historical Stock Prices: Retrieve historical stock prices from Yahoo Finance for the specified tickers.
- Calculate Volatility: Calculate daily and yearly volatility for each stock.
- Process Raw Volatility Data: Process raw volatility data and output the results to `volatility.csv`.
   
