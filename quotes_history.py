# -*- coding: utf-8 -*-
"""
Get quotesdf

@author: Dazhuang
"""

import requests
import re
import json
import pandas as pd
from datetime import date

def retrieve_quotes_historical(stock_code):
    quotes = []
    url = 'https://finance.yahoo.com/quote/%s/history?p=%s' % (stock_code, stock_code)
    r = requests.get(url)
    m = re.findall('"HistoricalPriceStore":{"prices":(.*?),"isPending"', r.text)
    if m:
        quotes = json.loads(m[0])
        quotes = quotes[::-1]
    return  [item for item in quotes if not 'type' in item]

quotes = retrieve_quotes_historical('IBM')
list1=[]
for i in range(len(quotes)):
    x = date.fromtimestamp(quotes[i]['date'])
    y=date.strftime(x,'%Y-%m-%d')
    list1.append(y)
quotesdf_ori=pd.DataFrame(quotes,index=list1)
quotesdf_m=quotesdf_ori.drop(['adjclose'],axis=1)
quotesdf=quotesdf_m.drop(['date'],axis=1)

#quotesdf = pd.DataFrame(quotes)

print(quotesdf)
"""
quotesdf[(quotesdf.index>='2017-03-01')&(quotesdf.index<='2017-03-31')]
quotesdf[(quotesdf.index>='2017-03-01')&(quotesdf.index<='2017-03-01')&(quotesdf.close<=80)]
"""