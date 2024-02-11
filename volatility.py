import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.core.common.is_list_like = pd.api.types.is_list_like 
import pandas_datareader as web
from datetime import datetime
from pandas_datareader import data, wb
import math

dataframe = pd.read_csv("your_stock_file.csv",sep=",",header=None)

n=len(dataframe.columns)
tickers = []
for i in range(n):
     tickers.insert(0, dataframe.loc[0][i])

start = datetime(2010, 1, 1)
end = datetime.today()
multpl_stocks = pd.DataFrame([data.DataReader(ticker, 'yahoo', start, end)['Adj Close'] for ticker in tickers]).T
multpl_stocks.columns = tickers

multpl_stocks = multpl_stocks.fillna(0)
multpl_stock_daily_returns = multpl_stocks.pct_change()
daily_vol = multpl_stock_daily_returns.std()
daily_vol = pd.DataFrame(daily_vol.fillna(0)).T
yearly_vol = math.sqrt(252) * daily_vol
yearly_vol = pd.DataFrame(yearly_vol.fillna(0)).T

rawvol = pd.read_csv("rawvolatility.csv",sep=",")
da=["Date"]
rawvol.columns = da+tickers
rawvol = rawvol.fillna(0)

yearly_vol = yearly_vol.T

drl=[]
for i in range(len(daily_vol.columns)):
     drl.insert(0, float(daily_vol.loc[0][i]))
drl.reverse()

yrl=[]
for i in range(len(yearly_vol.columns)):
     yrl.insert(0, float(yearly_vol.loc[0][i]))
yrl.reverse()

for i in range(len(rawvol)):
    k=0
    for j in range(1,len(rawvol.columns)):
        if i==0:
            if k<len(drl):
                rawvol.iloc[i,j]=drl[k] 
                k=k+1
        if i==1:
            if k<len(yrl):
                rawvol.iloc[i,j]=yrl[k] 
                k=k+1
                
rawvol.to_csv(r'your_volatility_output_target_file.csv', index = False, header=True)
