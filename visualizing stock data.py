import datetime as dt
import pandas_datareader as web
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mpl_finance import candlestick_ohlc
#Define Time Frame

start=dt.datetime(2020,4,1)
end=dt.datetime(2020,5,22)

#Load Date
data=web.DataReader('HDFCBANK.NS','yahoo',start,end)

#Restructure Data

data=data[['Open','High','Low','Close']]
data.reset_index(inplace=True)
data['Date']=data['Date'].map(mdates.date2num)

#Visualaization
ax=plt.subplot()
ax.grid(True)
ax.set_axisbelow(True)
ax.set_facecolor('black')
ax.figure.set_facecolor('#121212')
ax.tick_params(axis='x',colors='white')
ax.tick_params(axis='y',colors='white')
ax.xaxis_date()
candlestick_ohlc(ax,data.values,width=0.6,colorup ='#00ff00')
plt.show()