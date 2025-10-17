# -*- coding: utf-8 -*-
"""
Created on Fri Jun 27 13:36:21 2025

@author: vinda
"""

import datetime as dt
import yfinance as yf
import pandas as pd

end = dt.datetime.today()
start = end - dt.timedelta(3650)

stocks = ["INFY.NS","MSFT","PNB.NS","TCS.NS"]

data = pd.DataFrame()

for ticker in stocks:
    data[ticker] = yf.download(ticker,start,end)["Open"]
    
#filling nan value with fillna()
data.fillna(method="bfill",axis=0,inplace=True)
#inplace makes changes to tje original data in the table rather than just printing the copy with filled values.

data.mean()
data.describe()

#data.head() and data.tail() can be used
daily_return = data.pct_change()

#NOTE : data.shift() is used to shift the entire data frame by 1 row .

#calculating the aveeraeg daily return.
daily_return.mean()
daily_return.std()

#rolling means are used in indicators such as MA
df= daily_return.rolling(window=10).mean()

#To calculate exponential moving averages we use ewm( functio : exponential weighted)
df2 = daily_return.ewm(com=10, min_periods=10).mean()
#min_periods is to specify the minimum data points to calculate.

data.plot()
data.plot(subplots=True, layout=(2,2),sharex=True)

daily_return.plot(subplots=True)
(1+daily_return).cumprod().plot()
#cumulative product is to calculate the  gains