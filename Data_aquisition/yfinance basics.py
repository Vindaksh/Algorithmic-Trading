# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import datetime as dt
import yfinance as yf
import pandas as pd

end = dt.datetime.now()
start = end - dt.timedelta(hours=30)

stocks = ["INFY.NS","MSFT","PNB.NS","TCS.NS"]

data = {}

for ticker in stocks:
    data[ticker] = yf.download(ticker,start,end,interval="1m")