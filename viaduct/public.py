"""

Standard REST request handler that doesn't need any account specific details or Selenium session cookie extraction

"""

import logging

from viaduct.utils import *


class Public:
    def __init__(self, loadSymbols=False):
        if (loadSymbols):
            self.saveAllInstruments()
        else:
            self.loadedInstruments = False

    # Get all instruments on Trading212!
    def getAllInstruments(self):
        return get("https://live.trading212.com/rest/instruments/EQUITY/1")

    # Gets company ISINs and tickers for graphs etc
    def getTickers(self):
        return get("https://live.trading212.com/rest/companies")

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

    # Gets a symbols shortName
    def getShortName(self, isin="", fullName="", ticker="", id=""):
        if (isin != ""):
            return self.instrumentSearch("isin", isin, "shortName")
        if (fullName != ""):
            return self.instrumentSearch("fullName", fullName, "shortName")
        if (ticker != ""):
            return self.instrumentSearch("ticker", ticker, "shortName")
        if (id != ""):
            return self.instrumentSearch("id", id, "shortName")
        else:
            raise Exception(
                "ISIN, fullName, ticker, or id is required to find shortName")

    # Gets a symbols fullName
    def getFullName(self, isin="", shortName="", ticker="", id=""):
        if (isin != ""):
            return self.instrumentSearch("isin", isin, "fullName")
        if (shortName != ""):
            return self.instrumentSearch("shortName", shortName, "fullName")
        if (ticker != ""):
            return self.instrumentSearch("ticker", ticker, "fullName")
        if (id != ""):
            return self.instrumentSearch("id", id, "fullName")
        else:
            raise Exception(
                "ISIN, shortName, ticker, or id is required to find fullName")

    # Gets a symbols ticker
    def getTicker(self, isin="", shortName="", fullName="", id=""):
        if (isin != ""):
            return self.instrumentSearch("isin", isin, "ticker")
        if (shortName != ""):
            return self.instrumentSearch("shortName", shortName, "ticker")
        if (fullName != ""):
            return self.instrumentSearch("fullName", fullName, "ticker")
        if (id != ""):
            return self.instrumentSearch("id", id, "ticker")
        else:
            raise Exception(
                "ISIN, shortName, fullName, or id is required to find ticker")

    # Gets a symbols ISIN
    def getISIN(self, shortName="", fullName="", ticker="", id=""):
        if (shortName != ""):
            return self.instrumentSearch("shortName", shortName, "isin")
        if (fullName != ""):
            return self.instrumentSearch("fullName", fullName, "isin")
        if (ticker != ""):
            return self.instrumentSearch("ticker", ticker, "isin")
        if (id != ""):
            return self.instrumentSearch("id", id, "isin")
        else:
            raise Exception(
                "shortName, fullName, ticker, or id is required to find ISIN")

    # Get instrument details position ticker from the secret API
    def getInstrument(self, ticker):
        return get("https://live.trading212.com/rest/v2/instruments/" + ticker)

    # Get instrument details by ISIN
    # If language is not available, Trading212 seems to return English
    def getFundamentals(self, isin, langticker="en"):
        return get("https://live.trading212.com/rest/companies/fundamentals?languageticker=" + langticker + "&isin=" + isin)

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
        return post(url="https://live.trading212.com/charting/v2/batch", payload=payload)
