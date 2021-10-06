import pandas as pd
from financial_analysis.data import read_data
import matplotlib.pyplot as plt


# close_to_daily_return (確認資料為順時間排序)
def daily_return(df, start=None, end=None):
    df = df[['close']]
    df = df.loc[start:end]
    dr = df.pct_change(1)
    dr = dr.dropna()
    return dr


# daily_return_to_std (確認資料為順時間排序)
def r_std(dr, period=0):
    period_dr = dr.iloc[-period:-1]
    daily_std = period_dr.std()
    annual_std = daily_std * 252 ** 0.5
    rolling_annual_std = dr.rolling(252).std() * 252 ** 0.5
    rolling_annual_std = rolling_annual_std.dropna()
    result = {'daily_std': daily_std[0], 'annual_std': annual_std[0], 'rolling_annual_std': rolling_annual_std}
    return result


# daily_return_to_mdd (確認資料為順時間排序)
def mdd(dr):
    r = dr.add(1).cumprod()
    dd = r.div(r.cummax()).sub(1)
    mdd = dd.min()
    end = dd.idxmin()
    start = r.loc[:end[0]].idxmax()
    days = end - start
    result = {'mdd': mdd[0], 'start': start[0], 'end': end[0], 'days': days[0]}
    return result


def sharpe(dr):
    ar = dr.mean() * 252
    std = dr.std() * 252 ** 0.5
    sp = ar / std
    return sp[0]


def sortino(dr):
    ar = dr.mean() * 252
    std_s = dr[dr < 0].std() * 252 ** 0.5
    sp = ar / std_s
    return sp[0]


start = '2018-10-01'
end = '2021-10-01'

if __name__ == '__main__':
    spx_dr = daily_return(read_data('spx'), start=start, end=end)

    spx_mdd = mdd(spx_dr)
    spx_std = r_std(spx_dr)

    print(f'回測開始於 {start}, 回測結束於 {end}')
    print(f'最大跌幅 {spx_mdd["mdd"]:3.2%}, 起跌日 {spx_mdd["start"]:%Y-%m-%d}, 止跌日 {spx_mdd["end"]:%Y-%m-%d}, '
          f'下跌時間 {spx_mdd["days"]}')
    print(f'日波動 {spx_std["daily_std"]:3.2%}, 年化波動 {spx_std["annual_std"]:3.2%}')
    print(f'夏普比率 : {sharpe(spx_dr):.2f}')
    print(f'索提諾比率 : {sortino(spx_dr):.2f}')

# plt.plot(spx_std['rolling_annual_std'])
# plt.show()
