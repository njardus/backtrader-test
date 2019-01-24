from datetime import datetime
import backtrader as bt


class SmaCross(bt.SignalStrategy):
    params = (('pfast', 15), ('pslow', 50),)

    def __init__(self):
        sma1, sma2 = bt.ind.SMA(period=self.p.pfast), bt.ind.SMA(period=self.p.pslow)
        self.signal_add(bt.SIGNAL_LONG, bt.ind.CrossOver(sma1, sma2))


def grabdata(index):
    print(index)
    data = bt.feeds.YahooFinanceData(dataname=index, fromdate=datetime(2016, 1, 1),
                                     todate=datetime(2017, 12, 31))
    cerebro.adddata(data)


if __name__ == "__main__":
    cerebro = bt.Cerebro()

    uni = ["TBS.JO",
           "CPI.JO",
           "NPN.JO",
           "MNK.JO",
           "SNT.JO",
           "DSY.JO",
           "CLS.JO",
           "MND.JO",
           "AVI.JO",
           "AFX.JO",
           "MTA.JO",
           "FSR.JO",
           "TKG.JO",
           "IMP.JO",
           "SPP.JO"]

    for ticker in uni:
        grabdata(ticker)

    cerebro.addstrategy(SmaCross)
    cerebro.run()
    cerebro.plot()

