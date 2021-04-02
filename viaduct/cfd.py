from viaduct.core import *
from viaduct.utils import *


class CFD(CoreModule):
    def __init__(self, email, password, reality, browserPath, headless=False, timeout=2, loadSymbols=False):
        super().__init__(email, password, TradingType.CFD,
                         reality, headless, browserPath, timeout)
        self.reality = reality

    # Format url on whether is live
    def urlf(self, url):
        if (self.reality == Reality.Real):
            return ("https://live.trading212.com" + url)
        elif (self.reality == Reality.Practice):
            return ("https://demo.trading212.com" + url)
        else:
            raise Exception("Invalid reality " + self.reality)

    # Gets chart data for a particular ticker
    # When getting chart data, the ticker returned is the ticker not what is on the stock exchange!
    def getChartData(self, ticker, chartPeriod, size, includeFake=False):
        payload = {
            "candles": [
                {
                    "ticker": ticker,
                    "period": chartPeriod,
                    "size": size,
                    "includeFake": includeFake
                }
            ]
        }
        return post(url=self.urlf("/charting/v2/batch"), payload=payload)
