# -*- coding: utf-8 -*-
"""
Created on Wed Jul  2 13:57:32 2025

@author: vinda
"""

import yfinance as yf

tickers = ['MSFT','AAPL','GOOG']
ohlcv_data = {}

for ticker in tickers:
    temp = yf.download(ticker,period='1mo',interval='15m')
    temp.dropna(how='any',inplace=True)
    ohlcv_data[ticker] = temp
    
df = ohlcv_data["MSFT"]
    
def MACD(DF, a=12, b=26, c=9):
    df=DF.copy()
    df["ma_fast"]=df["Close"].ewm(span=a, min_periods=a).mean()
    df["ma_slow"]=df["Close"].ewm(span=b, min_periods=b).mean()
    df["MACD"]= df["ma_fast"] - df["ma_slow"]
    df["signal"]=df["MACD"].ewm(span=c, min_periods=c).mean()
    return df.loc[:,["MACD","signal"]]

for ticker in tickers:
    ohlcv_data[ticker][["macd","SIGNAL"]] = MACD(ohlcv_data[ticker])   