from viaduct.core import *
from viaduct.utils import *


class Equity(CoreModule):
    def __init__(self, email, password, reality, browserPath, headless=False, timeout=2):
        super().__init__(email, password, TradingType.Equity,
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

    # Gets min and max buy and sell value in £, max sell quantity is number of shares
    # Not sure what sellThreshold is
    # The sell parameters only appear for UK stocks for some reason
    def getMinMax(self, code):
        return super().get(self.urlf("/rest/v1/equity/value-order/min-max?instrumentCode=" + code), cookies=self.cookiePayload)

    # Takes instrument code, returns maxBuy and maxSell in shares for the account and max buy and sell that is technically
    # possible on the exchange, also has minTrade and if suspended
    def getSettings(self, code):
        return super().post(self.urlf("/rest/v2/account/instruments/settings"), cookies=self.cookiePayload, payload=[code])

    # Gets the account performance graph data
    def getPortfolioPerformance(self, historyPeriod):
        return super().get(self.urlf("/rest/v2/portfolio?period=" + historyPeriod), cookies=self.cookiePayload)
