<p align="center">
  <img src="https://github.com/harrytwigg/Viaduct-Trading212-Python-API/blob/main/images/Frontpage.jpg" width="400">
</p>

# Viaduct | A Trading212 Python REST API

Viaduct is a Python REST API wrapper that utilises Trading212's REST API that normally communciates exclusively with first party apps. This has not been offically released publicly but can be reverse-engineered.

Selenium is used to scrape required cookies and customer data from the web app but is no longer required after this point. REST network calls are used enabling greater functionallity and speed than pure web scraping.

The use of a wrapper ensures any API changes in the future will not impact pre-existing Trading212 dependeant programs as the wrapper itself can be updated instead of the underlying code.

## Prerequisites

- Firefox if not in default location, an error will be returned upon runtime.
- The Selenium Gecko driver will automatically install if not in system path, no manual installation is requried!

## Installation

Pip install out now!

```console
pip install viaduct
```

## Import and Usage

Viaduct is an API wrapper. API responses are returned python dictionaries, see the root tree images for more information. Selenium web scrapping modes extend the public class so it does not need to be recreated.

Examples are the payloads that the Rest API returns, these are returned as Python dictionaries for your convenience

Remember to disable 2-factor authentification and store passwords securely!

## Usage Key

See below for currently implemented API class methods, these are explained further below

| Method | Public | ISA | Equity | CFD |
| --- | --- | --- | --- | --- |
| 1 - getInstrument() | X | X | X | X |
| 2 - getAllInstruments() | X | X | X | X |
| 3 - getFundamentals() | X | X | X | X |
| 4 - getMinMax() |  | X | X |  |
| 5 - getSettings() |  | X | X |  |
| 6 - getChartData() | X | X | X | X |
| 7 - getPortfolioPerformance() |  | X | X |  |

## Public Mode

Retrieve publicly available information on companies and their financial information, utilises Trading212's unpublished private REST API no Selenium or web scrapping is required!

Symbols can be optionally loaded at startup, this will take approxuimately 30 seconds, this is requried for symbol reference conversion.

Symbol reference conversion refers to being able to use an isntruments name short hand, pretty name, code, ISIN (International Securities Identification Number), or ID. These are referred to in the Trading212 API and can be converted to one another through the use of helper functions. Code refers to the ticker identifier, name is a shorthand of the pretty name.

```python
instance = Public(loadSymbols=False)
```

## ISA Mode

Selenium powered wrapper for management of an ISA account, real mode only

If Firefox is not installed in default folder, make sure you pass the installed path upon initialisation:

```python
instance = ISA("email", "password", browserPath=r"C:\Program Files\Mozilla Firefox\firefox.exe")
```

## Equity Mode

Selenium powered wrapper for management of an Equity account, real or demo modes are supported

If Firefox is not installed in default folder, make sure you pass the installed path upon initialisation:

```python
instance = Equity("email", "password", reality=Reality.Real, browserPath=r"C:\Program Files\Mozilla Firefox\firefox.exe")
```

## CFD Mode

Selenium powered wrapper for management of CFD account, real or demo modes are supported

Custom methods for CFD are not yet supported and only return Public API calls

If Firefox is not installed in default folder, make sure you pass the installed path upon initialisation:

```python
instance = CFD("email", "password", reality=Reality.Real, browserPath=r"C:\Program Files\Mozilla Firefox\firefox.exe")
```

## API Class Methods

### 1 - getInstrument() - Get specific instrument details instead of all of them

```python
instance.getAllInstruments(code="TSLA")
```

Get instrument details using position code from the secret API, note this is not the shorthand name, ISIN or stock ticker. Ideal for updating existing data on a stock of interest. This is far faster than loading all instruments so if you know the isntrument code, then use this!

#### Example result [here](examples/1.json)

### 2 - getAllInstruments() - Get all securities on Trading212!

```python
instance.getAllInstruments()
```

This returns all the securities on Trading212 Equity and ISA, be warned it's over 9,000 and constantly growing

Result format is the same as a single instrument but returns a list of dictionaries

#### Example result [here](examples/2.json)

### 3 - getFundamentals() - Get company fundamentals

```python
instance.getFundamentals(isin="US36467W1099")
```

Takes an isin, returns a requested companies details

#### Example result [here](examples/3.json)

### 4 - getMinMax() - Get min and max position sizes

```python
instance.getMinMax(code="GYMl_EQ")
```

Takes a company code. Gets minBuy, maxBuy, minSell, maxSell values in £, maxSellQuantity is number of shares. Not sure what sellThreshold is. The sell parameters only appear for UK stocks for some reason.

#### Example result [here](examples/4.json)

### 5 - getSettings() - Get position trade settings

```python
instance.getSettings(code="BOOHl_EQ")
```

Takes instrument code, returns maxBuy and maxSell in shares for the account and max buy and sell that is technically possible on the exchange, also has minTrade and if the instrument is suspended.

#### Example result [here](examples/5.json)

### 6 - getChartData() - Get instrument chart data

```python
instance.getChartData(ticker="TSLA", chartPeriod=ChartPeriod.D1, number=5)
```

Takes an instrument ticker, called 'name' when getInstrument() is called, returns a dictionary of data that is normally exclusively displayed on price charts. also takes period and number of most recent data points to return

#### Example result [here](examples/6.json)

### 7 - getPortfolioPerformance() - Gets the account performance graph data

```python
instance.getPortfolioPerformance(historyPeriod=HistoryTimeframe.Y1):
```

This returns the account portfolio performance graph data that is displayed in the top left of the new app, takes a HistoryPeriod enumeration

#### Example result [here](examples/7.json)