import pandas as pd
from pandas.io.data import DataReader as DR
from datetime import datetime as dt
start=dt(2011,1,1)
end=dt(2015,6,1)
data=DR("4162.KL",'yahoo',start,end)

#I've saved data into a csv file to ease extraction of data via pandas
data.to_csv('data.ohlc.scv')

# I would like to read only specific columns of the data set at one time in order to calculate the moving averages for that particular column
df=pd.read_csv('data.ohlc.scv',index_col='Date',parse_dates=True)

# I want to simulate the moving averages of  "Open", "High", "Low", "Close"
# I'll be using the pandas library for simplification
df['5OPEN']=pd.rolling_mean(df['Open'],5)
df['5HIGH']=pd.rolling_mean(df['High'],5)
df['5LOW']=pd.rolling_mean(df['Low'],5)
df['5CLOSE']=pd.rolling_mean(df['Close'],5)

#To plot the moving averages
#Again using pandas
import matplotlib.pyplot as plt
df[['5OPEN','5HIGH','5LOW','5CLOSE']].plot();
plt.title('British American Tobacco Malaysia Bhd Moving Average Stock Prices')
plt.show()

#downloading data on FTSEKLCI
dataKLCI=DR("^KLSE", 'yahoo', start, end)
dataKLCI.to_csv('dataKLCI.ohlc.scv')
df2=pd.read_csv('dataKLCI.ohlc.scv',index_col='Date',parse_dates=True)

#Calculating correlation with BATM
df.corrwith(df2)
