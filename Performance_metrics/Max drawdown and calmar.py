# -*- coding: utf-8 -*-
"""
Created on Mon Jul  7 19:27:05 2025

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

def max_drawdown(DF):
    df = ohlcv_data[ticker].copy()
    df["return"] = df["Close"].pct_change()
    df["cum_return"] = (1+df["return"]).cumprod()
    df["cum_return"].plot()
    df["cum_roll_max"] = df["cum_return"].cummax()
    df["drawdown"] = df["cum_roll_max"] - df["cum_return"]
    df["drawdown_perc"] = df["drawdown"]/df["cum_roll_max"]
    return df["drawdown_perc"].max()

def calmar(DF):
    df=DF.copy()
    return CAGR(df)/max_drawdown(df)
    
for ticker in ohlcv_data:
    print("Max Drawdown for {} is {}".format(ticker, max_drawdown(ohlcv_data[ticker])))
    print("Calmar ratio for {} is {}".format(ticker, calmar(ohlcv_data[ticker])))