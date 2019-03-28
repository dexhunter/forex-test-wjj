import numpy as np
import pandas as pd
import pywt
import os


df = {}
#name = ['GBP_USD', 'NZD_USD', 'AUD_USD', 'USD_JPY', 'USD_DKK', 'USD_CAD', 'USD_CHF']
name = ['USD_DKK']
# read raw data
for i in range(len(name)):
    df[i] = pd.read_csv(name[i] + ".csv")
    df[i]['Date'] = pd.to_datetime(df[i]['Date'])
    df[i].set_index('Date', inplace=True)
    data_c = np.array(df[i]['Close'])

    # use DWT to transform a time series into a approximate part and a detailed part
    cA_c, cD_c = pywt.dwt(data_c,'db1')respectively

    #store data
    output1=pd.DataFrame([df[i],cA_c],index=['Close_cA'])
    output2=pd.DataFrame([df[i],cD_c],index=['Close_cD'])
    output1=output1.transpose()
    output2=output2.transpose()
    output1.to_csv(name[i]+'_cA.csv',index=False, sep=',')
    output2.to_csv(name[i]+'_cD.csv',index=False, sep=',')


