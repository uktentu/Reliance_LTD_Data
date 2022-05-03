import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime

import pandas_datareader.data as web

start = datetime.datetime(2021, 5, 3)   # past one years date
end = datetime.datetime(2022, 5, 3)    # todays date

realiance_df = web.DataReader(['RELIANCE.NS'], 'yahoo', start=start, end=end)['Close']
realiance_df.columns = {'Close Prices'}

# realiance_df.head(100)


realiance_df['20_SMA'] = realiance_df['Close Prices'].rolling(window=20,min_periods=1).mean()
realiance_df['50_SMA'] = realiance_df['Close Prices'].rolling(window=50,min_periods=1).mean()

# realiance_df.head()


realiance_df['Signal'] = 0.0
realiance_df['Signal'] = np.where(realiance_df['20_SMA']>realiance_df['50_SMA'],1.0,0.0)
realiance_df['Position'] = realiance_df['Signal'].diff()


# realiance_df.head()


#ploting the Dataframe 

plt.figure(figsize=(9,5))
realiance_df['Close Prices'].plot(color='k',label='Closing Prices')
realiance_df['20_SMA'].plot(color='b',label='20_SMA')
realiance_df['50_SMA'].plot(color='g',label='50_SMA')

plt.plot(realiance_df[realiance_df['Position'] == 1].index,realiance_df['20_SMA'][realiance_df['Position']==1],'^',markersize=10,color='g',label='buy')

plt.plot(realiance_df[realiance_df['Position'] == -1].index,realiance_df['20_SMA'][realiance_df['Position']==-1],'v',markersize=10,color='r',label='sell')

plt.legend()
plt.grid()
plt.title("Reliance Industries Limited - SMA",fontsize = 20 )
plt.ylabel("Prices in INR",fontsize = 15 )
plt.xlabel('Date', fontsize = 15 )
plt.show()


#Saving the dataframe work to excell
datatoexcell= pd.ExcelWriter('20_50_SMA.xlsx')
realiance_df.to_excel(datatoexcell)
datatoexcell.save()
