# -*- coding: utf-8 -*-
"""
Created on Wed Jun 25 21:18:53 2025

@author: vinda
"""

from alpha_vantage.timeseries import TimeSeries
import pandas as pd

key_path = r"D:\BITS_Acad\Algo trading\udemy\Alpha_vantage_API_key.txt"

ts = TimeSeries(key=open(key_path,'r').read(), output_format='pandas')
data = ts.get_daily(symbol="MSFT", outputsize='full')[0] #the [0] is to access only the data and avoiding the metadata
data.columns = ["open", "high", "low", "close", "volume"]

#to reverse the the whole dataframe so that it is first to latest
data = data.iloc[::-1]