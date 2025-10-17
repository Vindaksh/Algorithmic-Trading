# -*- coding: utf-8 -*-
"""
Created on Fri Jul  4 22:13:04 2025

@author: vinda
"""

import yfinance as yf
import pandas as pd
import numpy as np

tickers = ['MSFT','AAPL','GOOG']
ohlcv_data = {}
return_rate=[]

for ticker in tickers:
    temp = yf.download(ticker,period='12mo',interval='1d')
    temp.dropna(how='any',inplace=True)
    ohlcv_data[ticker] = temp
    
df=ohlcv_data["MSFT"]
    
def CAGR(DF):
    df2 = DF.copy()
    df2["return"] = df2["Close"].pct_change()
    df2["cum_return"] = (1+df2["return"]).cumprod()
    n=len(df)/252
    return float((df2["cum_return"].iloc[-1])**(1/n) - 1)

def VOLAT(DF):
    df = DF.copy()
    df["return"] = df["Close"].pct_change()
    vol = df["return"].std() * np.sqrt(252)
    #we are calculating for days in the year so 252 cahnge accordingly
    return vol

def sharpe(DF, rf=0.074):
    df = DF.copy()
    Sharpe = (CAGR(df)-rf)/VOLAT(df)
    return Sharpe

def sortino(DF, rf=0.074):
    df = DF.copy()
    df["return"] = df["Close"].pct_change()
    neg_return = np.where(df["return"]>0,0,df["return"])
    neg_volat = neg_return.std()
    return (CAGR(df)-rf)/neg_volat

for ticker in ohlcv_data:
    print("Sharpe for {} = {}".format(ticker, sharpe(ohlcv_data[ticker],0.03)))
    print("Sortino for {} = {}".format(ticker, sortino(ohlcv_data[ticker],0.03)))
