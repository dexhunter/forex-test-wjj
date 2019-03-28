import numpy as np
import pandas as pd
import pywt
import os


df = {}
name = ['GBP_USD', 'NZD_USD', 'AUD_USD', 'USD_JPY', 'USD_DKK', 'USD_CAD', 'USD_CHF']

# read raw data
for i in range(len(name)):
    df[i] = pd.read_csv(name[i] + ".csv")
    df[i]['Date'] = pd.to_datetime(df[i]['Date'])
    df[i].set_index('Date', inplace=True)
    data_c = np.array(df[i]['Close'])

    # use DWT to transform a time series into a approximate part and a detailed part respectively
    cA_c, cD_c = pywt.dwt(data_c,'db1')

    #store data
    output1=pd.DataFrame([df[i],cA_c],index=['Close_cA'],['Close_cD'])
    output1=output1.transpose()
    output1.to_csv(name[i]+'.csv',index=False, sep=',')
   


