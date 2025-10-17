# -*- coding: utf-8 -*-
"""
Created on Thu Jul  3 21:09:43 2025

@author: vinda
"""

import yfinance as yf
import numpy as np

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

def ADX(DF, n=20):
    df=DF.copy()
    df["ATR"] = ATR(df, n)
    df["upmove"] = df["High"] - df["High"].shift(1)
    df["downmove"] = df["Low"].shift(1)- df["Low"]
    df["+DM"] = np.where((df["upmove"]>df["downmove"]) & (df["upmove"]>0), df["upmove"], 0)
    df["-DM"] = np.where((df["downmove"]>df["upmove"]) & (df["downmove"]>0), df["downmove"], 0)
    df["+DI"] = 100* (df["+DM"]/df["ATR"]).ewm(com =n, min_periods=n).mean()
    df["-DI"] = 100* (df["-DM"]/df["ATR"]).ewm(com =n, min_periods=n).mean()
    df["ADX"] = 100* abs((df["+DI"] - df["-DI"])/(df["+DI"] + df["-DI"])).ewm(com =n, min_periods=n).mean()
    return df["ADX"]

for ticker in ohlcv_data:
    ohlcv_data[ticker]["ADX"] = ADX(ohlcv_data[ticker], 20)
