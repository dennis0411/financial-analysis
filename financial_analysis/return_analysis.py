import pandas as pd
from pandas_ods_reader import read_ods


#close_to_daily_return
def daily_return(symbol='spx', style='csv'):
    #注意資料為順時間排序
    if style == 'ods':
        df=read_ods(f'{symbol}.ods')
    else:
        df=pd.read_csv(f'{symbol}.csv')
    df.set_index(pd.to_datetime(df['Date']), inplace=True)
    df = df.sort_index()
    df.drop('Date', axis=1, inplace=True)
    dr=df.pct_change(1)
    return dr


#daily_return_to_mdd
def mdd(dr):
    # 注意資料為順時間排序
    r = dr.add(1).cumprod()
    dd = r.div(r.cummax()).sub(1)
    mdd = dd.min()
    end = dd.idxmin()
    start = r.loc[:end[0]].idxmax()
    days = end - start
    result = f'最大跌幅 {mdd[0]*100:3.2f}%, 起跌日 {start[0]:%Y-%m-%d}, 止跌日 {end[0]:%Y-%m-%d}, 下跌時間 {days[0]}'
    return result

spx = daily_return('spx','ods')
spx_mdd = mdd(spx)
print(spx)
print(spx_mdd)


