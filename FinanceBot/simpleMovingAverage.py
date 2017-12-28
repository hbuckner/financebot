from readCurrency import readCurrency
import pandas as pandas
from pandas_datareader import data as web
import datetime
from datetime import datetime, timedelta
import numpy as np 
import fix_yahoo_finance as yf
yf.pdr_override()
c=readCurrency().currencyGet("NASDAQ.txt")

def simpleMovingAverage(stockname):
	N = 365
	start = datetime.now() - timedelta(days=N)
	yesterday = datetime.today()-timedelta(days=1)
	end = yesterday
	
#searches list and calculates the average.
	stock = web.get_data_yahoo(stockname,start,end)
	#print(stock)
	if stock.empty==False:
		stock["20d"] = np.round(stock['Adj Close'].rolling(window = 200, center = False).mean(), 2)
		date = yesterday.strftime('%Y-%m-%d')
		todaystock=stock["20d"].tail(1)
		SMA=todaystock.ix[0,date]
		return SMA