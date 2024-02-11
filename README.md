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
    - Ensure you have historical stock price data available. The script retrieves data from Yahoo Finance using pandas_datareader.
      
2. Running the Script:
    - Run the Python script stock_volatility.py.
    - The script will calculate daily and yearly volatility for each stock using historical price data and output the results to a CSV file named volatility.csv.
  
3. Output:
    - The output CSV file volatility.csv contains the calculated daily and yearly volatility for each stock.
   
