"""

Utilities and basic framework for multiple features

"""


from time import sleep

import json
import requests

# Try clicking something until it works
def force_click(element, sleep_time=1):
    while True:
        try:
            element.click()
            return
        except:
            sleep(sleep_time)

def post(url, cookies="", payload=""):
    headers = {'Cookie': cookies, 'Connection': 'keep-alive',
               'Pragma': 'no-cache',
               'Cache-Control': 'no-cache',
               'Accept': 'application/json',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36',
               'Content-Type': 'application/json',
               'Sec-GPC': '1',
               'Origin': 'https://live.trading212.com',
               'Sec-Fetch-Site': 'same-origin',
               'Sec-Fetch-Mode': 'cors',
               'Sec-Fetch-Dest': 'empty',
               'Referer': 'https://live.trading212.com/beta',
               'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8'}
    
    response = requests.post(url, headers=headers,
                             data=json.dumps(payload))

    # response.headers is the response headers as x is the response
    # response.status code is number kind of response code

    # print(response.headers)

    if response.status_code == 400:
        raise Exception("Error 400 we made a bad requst")
    elif response.status_code == 404:
        raise Exception("Error 404 url not found")
    elif response.status_code == 401:
        raise Exception("Error 401 we are not authorised on Trading212")
    elif response.status_code == 500:
        raise Exception(
            "Error 500 Trading212 experienced an internal server error")
    elif response.status_code == 200:
        try:
            return json.loads(response.text)
        except:
            raise Exception(
                "No response body was received from the server")
    else:
        raise Exception("Error " + str(response.status_code) +
                        " encountered, unknown error")


def get(url, cookies="", payload=""):
    headers = {'Cookie': cookies, 'Connection': 'keep-alive',
               'Pragma': 'no-cache',
               'Cache-Control': 'no-cache',
               'Accept': 'application/json',
               'X-Trader-SeqId': '25',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36',
               'Content-Type': 'application/json',
               'Sec-GPC': '1',
               'Origin': 'https://live.trading212.com',
               'Sec-Fetch-Site': 'same-origin',
               'Sec-Fetch-Mode': 'cors',
               'Sec-Fetch-Dest': 'empty',
               'Referer': 'https://live.trading212.com/beta',
               'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8'}
    
    response = requests.get(url, headers=headers, data=json.dumps(payload))

    # response.headers is the response headers as x is the response
    # response.status code is number kind of response code
    
    # print(response.headers)

    if response.status_code == 400:
        raise Exception("Error 400 we made a bad requst")
    elif response.status_code == 404:
        raise Exception("Error 404 url not found")
    elif response.status_code == 401:
        raise Exception("Error 401 we are not authorised on Trading212")
    elif response.status_code == 200:
        try:
            return json.loads(response.text)
        except:
            raise Exception("No response body was received from the server")
    else:
        raise Exception("Error " + str(response.status_code) +
                        " encountered, unknown error")

# Enumerations


class TradingType:
    CFD = "CFD"
    Equity = "EQUITY"
    ISA = "ISA"


class Reality:
    Practice = "PRACTICE"
    Real = "REAL"


class BuyStockMethod:
    Shares = "Shares"
    Value = "Value"


class ChartPeriod:
    m1 = "ONE_MINUTE"
    m5 = "FIVE_MINUTES"
    m10 = "TEN_MINUTES"
    m15 = "FIFTEEN_MINUTES"
    m30 = "THIRTY_MINUTES"
    H1 = "ONE_HOUR"
    H4 = "FOUR_HOURS"
    D1 = "ONE_DAY"
    W1 = "ONE_WEEK"
    M1 = "ONE_MONTH"


class HistoryTimeframe:
    D1 = "LAST_DAY"
    W1 = "LAST_WEEK"
    M1 = "LAST_MONTH"
    M3 = "LAST_THREE_MONTHS"
    Y1 = "LAST_YEAR"
    ALL = "ALL"
