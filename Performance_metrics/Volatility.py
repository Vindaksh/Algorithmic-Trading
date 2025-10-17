# -*- coding: utf-8 -*-
"""
Created on Fri Jul  4 22:00:13 2025

@author: vinda
"""

import yfinance as yf
import numpy as np

tickers = ['MSFT','AAPL','GOOG']
ohlcv_data = {}
return_rate=[]

for ticker in tickers:
    temp = yf.download(ticker,period='12mo',interval='1d')
    temp.dropna(how='any',inplace=True)
    ohlcv_data[ticker] = temp
    
    
def VOLAT(DF):
    df = DF.copy()
    df["return"] = df["Close"].pct_change()
    vol = df["return"].std() * np.sqrt(252)
    #we are calculating for days in the year so 252 cahnge accordingly
    return vol

for ticker in ohlcv_data:
    print("Volatility of {} = {}".format(ticker, VOLAT(ohlcv_data[ticker])))