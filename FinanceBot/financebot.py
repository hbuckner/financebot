from readCurrency import readCurrency
c=readCurrency().currencyGet("NASDAQ.txt")
import pandas as pandas
from pandas_datareader import data as web
import datetime
from datetime import datetime, timedelta
from simpleMovingAverage import simpleMovingAverage 
list=[]

#SMA = SimpleMovingAverage.simpleMovingAverage(x)
for x in c:
	print()
	SMA = simpleMovingAverage(x)
	list.append([x,SMA])
	#print(SMA)

with open('SMA.txt','w') as f:
	for item in list:
		print>>f, item
	f.close()