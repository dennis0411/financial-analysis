import pandas as pd
import numpy as np
import requests
import xlsxwriter
import math


# IEX Cloud api
ticker = 'AAPL'
api_url = f'https://sandbox.iexapis.com/stable/stock/{ticker}/quote?token={IEX_CLOUD_API_TOKEN}'
data = requests.get(api_url).json()
print(data)

# 指數成員
stocks = pd.read_csv('sp_500_stocks.csv')
