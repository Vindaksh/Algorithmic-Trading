# -*- coding: utf-8 -*-
"""
Created on Wed Jul  2 22:30:16 2025

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

def bollinger_band(DF, n=20):
    df=DF.copy()
    df["MB"]=df["Close"].rolling(n).mean()
    df["LB"]=df["Close"] - 2*df["Close"].rolling(n).std(ddof=0)
    #ddof= degree of freedom (when std is calculated for single values denominator is n-1, but for a population it is n do ddof=0)
    df["UB"]=df["Close"] + 2*df["Close"].rolling(n).std(ddof=0)
    df["BB_width"] = df["UB"] - df["LB"]
    return df[["UB","MB","LB","BB_width"]]

for ticker in ohlcv_data:
    ohlcv_data[ticker][["UB","MB","LB","BB_width"]] = bollinger_band(ohlcv_data[ticker])
    
    