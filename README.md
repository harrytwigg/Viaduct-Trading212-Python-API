<p align="center">
  <img src="https://github.com/harrytwigg/Viaduct-Trading212-Python-API/blob/main/images/Frontpage.jpg" width="400">
</p>

# Viaduct | A Trading212 Python REST API

Viaduct is a Python REST API that utilises Trading212's REST API that normally communciates exclusively with first party apps. Selenium is used to scrape required cookies and customer data from the web app but is no longer required after this point. REST network calls are used enabling greater functionallity and speed than pure web scraping.

## Installation and Setup

### Prerequisites

- Firefox if not in default location, an error will be returned upon runtime.
- The Selenium Gecko driver will automatically install if not in system path, no manual installation is requried!

Pip install coming soon!

### Import and Usage

If Firefox is not installed in default folder, make sure you pass it upon initialisation for example:

```python
instance = viaduct.ISA(email, password, Reality.Real, browserPath=r"C:\Program Files\Mozilla Firefox\firefox.exe")
```

Currently only ISA Mode is supported, more are coming soon
Responses are returned python dictionaries, see the root tree images for more information

### ISA Mode

### A1) getInstrument() - Get Specific Instrument Details Not All of Them

```python
instance.getAllInstruments(code="TSLA")
```

Get instrument details using position code from the secret API, note this is not the shorthand name, ISIN or stock ticker. Ideal for updating existing data on a stock of interest

#### Example result [here](examples/A/A1.json)

### A2) getAllInstruments() - Get all Securities on Trading212!

```python
instance.getAllInstruments()
```

This returns all the securities on Trading212 Equity and ISA, be warned it's over 9,000 and constantly growing

Result format is the same as a single instrument but returns a list of dictionaries

#### Example result [here](examples/A/A2.json)

### A3) getFundamentals() - Get Company Fundamentals

```python
instance.getFundamentals(isin="US36467W1099")
```

Takes an isin, returns a requested companies details

#### Example result [here](examples/A/A3.json)

### A4) getMinMax() - Get Min and Max Position Sizes

```python
instance.getMinMax(code="GYMl_EQ")
```

Takes a company code. Gets minBuy, maxBuy, minSell, maxSell values in £, maxSellQuantity is number of shares. Not sure what sellThreshold is. The sell parameters only appear for UK stocks for some reason.

#### Example result [here](examples/A/A4.json)

### A5) getSettings() - Get Position Trade Settings

```python
instance.getSettings(code="BOOHl_EQ")
```

Takes instrument code, returns maxBuy and maxSell in shares for the account and max buy and sell that is technically possible on the exchange, also has minTrade and if the instrument is suspended.

#### Example result [here](examples/A/A5.json)

### A6) getChartData() - Get Instrument Chart Data

```python
instance.getChartData(ticker="TSLA", chartPeriod=ChartPeriod.D1, number=5)
```

Takes an instrument ticker, called 'name' when getInstrument() is called, returns a dictionary of data that is normally exclusively displayed on price charts. also takes period and number of most recent data points to return

#### Example result [here](examples/A/A6.json)