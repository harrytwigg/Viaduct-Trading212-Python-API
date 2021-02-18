from viaduct.core import *
from viaduct.utils import *


class CFD(CoreModule):
    def __init__(self, email, password, reality, browserPath, headless=False, timeout=2):
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
