import backtrader as bt
from financial_analysis.data import read_data
import datetime
from financial_analysis import Strategy

data = read_data('spx')
start = datetime.datetime(2019, 1, 1)
end = datetime.datetime(2021, 10, 1)
test_data = bt.feeds.PandasData(dataname=data,
                                fromdate=start,
                                todate=end)
cerebro = bt.Cerebro()
cerebro.broker.setcash(1000000)
cerebro.broker.setcommission(0.001)


if __name__ == '__main__':
    print(f'Start Portfolio : {cerebro.broker.getvalue():,.2f}')
    cerebro.adddata(test_data)
    cerebro.addstrategy(Strategy.AverageStrategy, maperiod=20)
    cerebro.run()
    print(f'Final Portfolio : {cerebro.broker.getvalue():,.2f}')
    cerebro.plot()





