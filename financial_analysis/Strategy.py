import backtrader as bt


# 策略範例
class TestStrategy(bt.Strategy):
    params = (
        ('exitbars', 5),
    )

    def __init__(self):
        self.dataclose = self.datas[0].close
        self.order = None

    # 檢視訂單狀態，可以看出 Buy 是發生在下一根的 open
    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log(f'Buy Executed {order.executed.price}')
            if order.issell():
                self.log(f'Sell Executed {order.executed.price}')
            self.bar_executed = len(self)
        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log('Order Canceled/Margin/Rejected')
        self.order = None

    def next(self):
        self.log('Close {}'.format(self.dataclose[0]))
        if self.order:
            return
        if not self.position:
            if self.dataclose[0] < self.dataclose[-1]:
                if self.dataclose[-1] < self.dataclose[-2]:
                    self.log(f'Buy Create {self.dataclose[0]}')
                    self.order = self.buy()
        else:
            if len(self) >= (self.bar_executed + self.params.exitbars):
                self.log(f'Sell Create {self.dataclose[0]}')
                self.order = self.sell()

    def log(self, txt):
        dt = self.datas[0].datetime.date(0)
        print(f'{dt.isoformat()} {txt}')


# 均線策略
class AverageStrategy(bt.Strategy):
    params = (
        ('maperiod', 15),
    )

    def __init__(self):
        self.dataclose = self.datas[0].close
        self.order = None
        self.sma = bt.indicators.MovingAverageSimple(self.datas[0], period=self.params.maperiod)

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log(f'Buy Executed {order.executed.price}')
            if order.issell():
                self.log(f'Sell Executed {order.executed.price}')
            self.bar_executed = len(self)
        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log('Order Canceled/Margin/Rejected')
        self.order = None

    def next(self):
        self.log('Close {}'.format(self.dataclose[0]))
        if self.order:
            return
        if not self.position:
            if self.dataclose[0] > self.sma[0]:
                self.log(f'Buy Create {self.dataclose[0]}')
                self.order = self.buy()

        else:
            if self.dataclose[0] < self.sma[0]:
                self.log(f'Sell Create {self.dataclose[0]}')
                self.order = self.sell()

    def log(self, txt):
        dt = self.datas[0].datetime.date(0)
        # print(f'{dt.isoformat()} {txt}')

    def stop(self):
        print(f'maperiod= {self.params.maperiod}, portfolio= {self.broker.getvalue():,.2f}')
