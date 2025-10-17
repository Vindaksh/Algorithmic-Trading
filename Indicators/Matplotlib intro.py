# -*- coding: utf-8 -*-
"""
Created on Fri Jun 27 19:57:06 2025

@author: vinda
"""

import datetime as dt
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

end = dt.datetime.today()
start = end - dt.timedelta(3650)

stocks = ["INFY.NS","MSFT","PNB.NS","TCS.NS"]

data = pd.DataFrame()

for ticker in stocks:
    data[ticker] = yf.download(ticker,start,end)["Open"]
    
#filling nan value with fillna()
data.fillna(method="bfill",axis=0,inplace=True)

daily_return = data.pct_change()

fig, ax= plt.subplots()
ax.set(title="Plots using matplotlib", xlabel="stocks", ylabel="Return")
plt.bar(x=daily_return.columns, height=daily_return.mean() )
