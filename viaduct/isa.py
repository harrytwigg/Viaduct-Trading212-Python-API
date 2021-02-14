import json

from viaduct.core import *
from viaduct.utils import *


class ISA(CoreModule):
    def __init__(self, username, password, reality, browserPath, headless=False, timeout=2):
        super().__init__(username, password, TradingType.ISA,
                         reality, headless, browserPath, timeout)

    # Gets min and max buy and sell value in £, max sell quantity is number of shares
    # Not sure what sellThreshold is
    # The sell parameters only appear for UK stocks for some reason
    def getMinMax(self, code):
        return self.get("https://live.trading212.com/rest/v1/equity/value-order/min-max?instrumentCode=" + code, cookies=self.cookiePayload)

    # Takes instrument code, returns maxBuy and maxSell in shares for the account and max buy and sell that is technically
    # possible on the exchange, also has minTrade and if suspended
    def getSettings(self, code):
        return self.post("https://live.trading212.com/rest/v2/account/instruments/settings", cookies=self.cookiePayload, payload=[code])

    # Gets chart data fior a given ticker code
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
        return post("https://live.trading212.com/charting/v2/batch", cookies=self.cookiePayload, payload=payload)
    
    # Gets the account performance graph data
    def getPortfolioPerformance(self, historyPeriod):
        return get("https://live.trading212.com/rest/v2/portfolio?period=" + historyPeriod, cookies=self.cookiePayload)