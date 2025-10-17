# -*- coding: utf-8 -*-
"""
Created on Wed Jul  2 21:52:54 2025

@author: vinda
"""

import yfinance as yf

tickers = ['MSFT','AAPL','GOOG']
ohlcv_data = {}

for ticker in tickers:
    temp = yf.download(ticker,period='1mo',interval='5m')
    temp.dropna(how='any',inplace=True)
    ohlcv_data[ticker] = temp
    
df = ohlcv_data["MSFT"]

def ATR(DF, n=14):
    df = DF.copy()
    df["H-L"] = df["High"] - df["Low"]
    df["H-PC"] =  df["High"] - df["Close"].shift(1)
    df["L-PC"] =  df["Low"] - df["Close"].shift(1)
    df["TR"] = df[["H-L","H-PC","L-PC"]].max(axis=1,skipna=False)
    df["ATR"] = df["TR"].ewm(span=n, min_periods=n).mean()
    return df["ATR"]

for ticker in ohlcv_data:
    ohlcv_data[ticker]["ATR"] = ATR(ohlcv_data[ticker])