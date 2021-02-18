from viaduct.core import *
from viaduct.utils import *


class ISA(CoreModule):
    def __init__(self, email, password, browserPath, headless=False, timeout=2, loadSymbols=False):
        super().__init__(email, password, TradingType.ISA,
                         Reality.Real, headless, browserPath, timeout)
        self.reality = Reality.Real

        if (loadSymbols):
            self.saveAllInstruments()
        else:
            self.loadedInstruments = False

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
        return get(self.urlf("/rest/v1/equity/value-order/min-max?instrumentCode=" + code), cookies=self.cookiePayload)

    # Takes instrument code, returns maxBuy and maxSell in shares for the account and max buy and sell that is technically
    # possible on the exchange, also has minTrade and if suspended
    def getSettings(self, code):
        return post(self.urlf("/rest/v2/account/instruments/settings"), cookies=self.cookiePayload, payload=[code])

    # Gets the account performance graph data
    def getPortfolioPerformance(self, historyPeriod):
        return get(self.urlf("/rest/v2/portfolio?period=" + historyPeriod), cookies=self.cookiePayload)

    # Get all instruments on Trading212!
    def getAllInstruments(self):
        return get(self.urlf("/rest/v2/instruments/"))

    # Gets company ISINs and tickers for graphs etc
    def getTickers(self):
        return get(self.urlf("/rest/companies"))

    # Saves all instruments in a dictionary useful for symbol lookup
    def saveAllInstruments(self):
        logging.info("Loading all instruments, this will take a while...")
        self.instruments = self.getAllInstruments()
        # Don't think getting tickers is actually required
        #self.tickerISINs = self.getTickers()
        self.loadedInstruments = True

    # Search the instrument dictionary
    def instrumentSearch(self, searchUsing, searchKey, resultUsing):
        if (not self.loadedInstruments):
            self.saveAllInstruments()
        for i in self.instruments:
            try:
                if (i[searchUsing] == searchKey):
                    return i[resultUsing]
            except:
                pass

    # Gets a symbols name
    def getName(self, isin="", prettyName="", code="", id=""):
        if (isin != ""):
            return self.instrumentSearch("isin", isin, "name")
        if (prettyName != ""):
            return self.instrumentSearch("prettyName", prettyName, "name")
        if (code != ""):
            return self.instrumentSearch("code", code, "name")
        if (id != ""):
            return self.instrumentSearch("id", id, "name")
        else:
            raise Exception(
                "ISIN, prettyName, code, or id is required to find name")

    # Gets a symbols prettyName
    def getPrettyName(self, isin="", name="", code="", id=""):
        if (isin != ""):
            return self.instrumentSearch("isin", isin, "prettyName")
        if (name != ""):
            return self.instrumentSearch("name", name, "prettyName")
        if (code != ""):
            return self.instrumentSearch("code", code, "prettyName")
        if (id != ""):
            return self.instrumentSearch("id", id, "prettyName")
        else:
            raise Exception(
                "ISIN, name, code, or id is required to find prettyName")

    # Gets a symbols code
    def getCode(self, isin="", name="", prettyName="", id=""):
        if (isin != ""):
            return self.instrumentSearch("isin", isin, "code")
        if (name != ""):
            return self.instrumentSearch("name", name, "code")
        if (prettyName != ""):
            return self.instrumentSearch("prettyName", prettyName, "code")
        if (id != ""):
            return self.instrumentSearch("id", id, "code")
        else:
            raise Exception(
                "ISIN, name, prettyName, or id is required to find code")

    # Gets a symbols ISIN
    def getISIN(self, name="", prettyName="", code="", id=""):
        if (name != ""):
            return self.instrumentSearch("name", name, "isin")
        if (prettyName != ""):
            return self.instrumentSearch("prettyName", prettyName, "isin")
        if (code != ""):
            return self.instrumentSearch("code", code, "isin")
        if (id != ""):
            return self.instrumentSearch("id", id, "isin")
        else:
            raise Exception(
                "Name, prettyName, code, or id is required to find ISIN")

    # Gets a symbols ID
    def getID(self, isin="", name="", prettyName="", code=""):
        if (isin != ""):
            return self.instrumentSearch("isin", isin, "id")
        if (name != ""):
            return self.instrumentSearch("name", name, "id")
        if (prettyName != ""):
            return self.instrumentSearch("prettyName", prettyName, "id")
        if (code != ""):
            return self.instrumentSearch("code", code, "id")
        else:
            raise Exception(
                "ISIN, name, prettyName, or code is required to find id")

    # Get instrument details position code from the secret API
    def getInstrument(self, code):
        return get(self.urlf("/rest/v2/instruments/" + code))

    # Get instrument details by ISIN
    # If language is not available, Trading212 seems to return English
    def getFundamentals(self, isin, langCode="en"):
        return get(self.urlf("/rest/companies/fundamentals?languageCode=" + langCode + "&isin=" + isin))

    # Gets chart data for a particular ticker
    # When getting chart data, the ticker returned is the code not what is on the stock exchange!
    def getChartData(self, code, chartPeriod, size, includeFake=False):
        payload = {
            "candles": [
                {
                    "ticker": code,
                    "period": chartPeriod,
                    "size": size,
                    "includeFake": includeFake
                }
            ]
        }
        return post(url=self.urlf("/charting/v2/batch"), payload=payload)
