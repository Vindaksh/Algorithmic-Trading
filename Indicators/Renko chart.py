# -*- coding: utf-8 -*-
"""
Created on Thu Jul  3 21:38:16 2025

@author: vinda
"""

import yfinance as yf
from stocktrends import Renko

tickers = ['MSFT','AAPL','GOOG']
ohlcv_data = {}
hour_data = {}
renko_data = {}

for ticker in tickers:
    temp = yf.download(ticker,period='1mo',interval='5m')
    temp.dropna(how='any',inplace=True)
    ohlcv_data[ticker] = temp
    
    temp = yf.download(ticker,period='1y',interval='1h')
    temp.dropna(how='any',inplace=True)
    hour_data[ticker] = temp
    
def ATR(DF, n=14):
    df = DF.copy()
    df["H-L"] = df["High"] - df["Low"]
    df["H-PC"] =  df["High"] - df["Close"].shift(1)
    df["L-PC"] =  df["Low"] - df["Close"].shift(1)
    df["TR"] = df[["H-L","H-PC","L-PC"]].max(axis=1,skipna=False)
    df["ATR"] = df["TR"].ewm(span=n, min_periods=n).mean()
    return df["ATR"]

def renko_DF(DF, hourly_df):
    df = DF.copy()
    df.reset_index(inplace=True)
    df.columns = ["date","open","high","low","close","volume"]
    df2 = Renko(df)
    df2.brick_size = 3* round(ATR(hourly_df, 120).iloc[-1], 0)
    renko_df = df2.get_ohlc_data()
    return renko_df

for ticker in ohlcv_data:
    renko_data[ticker]= renko_DF(ohlcv_data[ticker], hour_data[ticker])