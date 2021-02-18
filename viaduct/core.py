"""

Shared core Selenium module

"""

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import logging

from viaduct.installer import *
from viaduct.utils import *
from viaduct.public import *


class CoreModule(Public):
    def __init__(self, username, password, tradingType, reality, headless, browserPath, timeout):
        super().__init__()

        installDriver()
        options = webdriver.FirefoxOptions()
        options.headless = headless
        options.binary_location = browserPath

        self.timeout = timeout
        self.reality = reality
        self.tradingType = tradingType

        self.driver = webdriver.Firefox(firefox_options=options)

        self.driver.get("https://www.trading212.com/en/login")
        sleep(1)
        self.driver.find_element_by_id("username-real").send_keys(username)
        sleep(0.2)
        self.driver.find_element_by_id("pass-real").send_keys(password)
        sleep(0.4)
        WebDriverWait(self.driver, self.timeout * 5).until(
            expected_conditions.element_to_be_clickable((By.CLASS_NAME, "button-login"))).click()
        sleep(0.4)

        # Cookies are required to make some requests, once acquired selenium no longer required!
        # Initial cookies are acquired for the setup
        self.cookiePayload = self.getCookies()

        # Get account data
        # self.accountData = self.get("https://live.trading212.com/frontend-data/customers/entries")
        # self.initInfo = self.get("https://live.trading212.com/rest/v3/init-info")

        self.getCorrectView()

        # Get the cookies again for the new view
        self.cookiePayload = self.getCookies()

    # Gets the current cookies
    def getCookies(self):
        rawCookies = self.driver.get_cookies()
        toReturn = rawCookies[0]["name"] + \
            '=' + rawCookies[0]["value"] + ';'
        for row in rawCookies[1:]:
            toReturn = toReturn + \
                ' ' + row["name"] + '=' + row["value"] + ';'
        return toReturn

    # Route urls based off of Reality
    def rURL(self, path=""):
        if (self.reality == Reality.Real):
            return "https://live.trading212.com/" + path
        elif (self.reality == Reality.Practice):
            return "https://demo.trading212.com/" + path
        else:
            raise Exception("Invalid reality: " + self.reality)

    def getCorrectView(self):
        # Get the correct reality
        if (self.driver.current_url != self.rURL()):
            self.driver.get(self.rURL())
        try:
            force_click(WebDriverWait(self.driver, self.timeout * 2).until(
                expected_conditions.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div[3]/div[2]"))))
        except:
            logging.warn("Didn't shut the new account view")

        # Switch to correct TradingType
        try:
            force_click(WebDriverWait(self.driver, self.timeout * 2).until(
                expected_conditions.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div[2]/div[3]"))))
            if (self.tradingType == TradingType.ISA):
                force_click(WebDriverWait(self.driver, self.timeout * 2).until(
                    expected_conditions.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[10]/div/div/div/div/div[1]/div/div[1]/div[3]"))))
            elif (self.tradingType == TradingType.Equity):
                force_click(WebDriverWait(self.driver, self.timeout * 2).until(
                    expected_conditions.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[10]/div/div/div/div/div[1]/div/div[1]/div[2]"))))
            elif (self.tradingType == TradingType.CFD):
                force_click(WebDriverWait(self.driver, self.timeout * 2).until(
                    expected_conditions.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[10]/div/div/div/div/div[1]/div/div[1]/div[1]"))))
            else:
                raise Exception("Invalid tradingType: " + self.tradingType)
        except:
            pass

        try:
            force_click(WebDriverWait(self.driver, self.timeout * 2).until(
                expected_conditions.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[5]"))))
            if (self.tradingType == TradingType.ISA):
                force_click(WebDriverWait(self.driver, self.timeout * 2).until(
                    expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="isaSwitchButton"]'))))
            elif (self.tradingType == TradingType.Equity):
                force_click(WebDriverWait(self.driver, self.timeout * 2).until(
                    expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="equitySwitchButton"]'))))
            elif (self.tradingType == TradingType.CFD):
                force_click(WebDriverWait(self.driver, self.timeout * 2).until(
                    expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="cfdSwitchButton"]'))))
        except:
            pass

        # If tradingType is not CFD request the new web app
        if (self.tradingType != TradingType.CFD):
            # Check if already using beta
            try:
                if (self.driver.current_url[:-4] != "beta"):
                    # Get beta
                    url = self.rURL("frontend-data/customers/entries")
                    payload = "[{\"key\":\"platform-pref\",\"value\":\"new\"}]"
                    get(url=url, payload=payload, cookies=self.cookiePayload)
                    self.driver.get(self.rURL("beta"))
            except:
                pass
            # Todo handle isa or equity
        else:
            # Todo handle CFD
            1
