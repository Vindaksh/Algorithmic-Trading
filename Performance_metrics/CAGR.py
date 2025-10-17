# -*- coding: utf-8 -*-
"""
Created on Fri Jul  4 21:33:01 2025

@author: vinda
"""

import yfinance as yf

tickers = ['MSFT','AAPL','GOOG']
ohlcv_data = {}
return_rate=[]

for ticker in tickers:
    temp = yf.download(ticker,period='12mo',interval='1d')
    temp.dropna(how='any',inplace=True)
    ohlcv_data[ticker] = temp
    
    
def CAGR(DF):
    df = ohlcv_data[ticker].copy()
    df["return"] = df["Close"].pct_change()
    df["cum_return"] = (1+df["return"]).cumprod()
    n=len(df)/252
    CAGR = float((df["cum_return"].iloc[-1])**(1/n) - 1)
    return CAGR

for ticker in ohlcv_data:
    print("CAGR for {} = {}".format(ticker, CAGR(ohlcv_data[ticker])))
