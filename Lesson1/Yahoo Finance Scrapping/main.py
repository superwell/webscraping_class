import selenium
import time
from selenium import webdriver
import pandas as pd


def greeting():
    print("Welcome to Tech Valley!")
    time.sleep(2)
    print("Today I would like to show you how I can capture Finance Data from Yahoo!")
    time.sleep(1)
    return 0


def ask_scrap_mode():
    mode = int(input("Enter 1 for specific ticker code, 2 for getting 0001 to 0050: "))
    return mode


def ticker_gen(range_num):
    data =[]
    for i in range(1,range_num):
        to_add = 4 - len(str(i))
        data.append("0"*to_add + str(i))
    return data


def get_specific():
    ticker = input("Please Enter the Stock Code you want: ")
    print("Please wait a moment, I will go Yahoo for the data!")
    driver = webdriver.Chrome()
    url = "https://hk.finance.yahoo.com/quote/{}.HK/history?p={}.HK".format(ticker, ticker)
    driver.get(url)

    table = driver.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody')
    rows = table.text.split("\n")
    data = []
    for row in rows:
        data.append(row.split(" "))
    header = ["Date", "Open", "High","Low", "Close", "Adj Close", "Volume"]
    df = pd.DataFrame(data, columns = header)

    df.to_excel("data/{}.xlsx".format(ticker), index=None)


def get_all():
    print("Let me do everything for you!")
    ticker_list = ticker_gen(51)
    driver = webdriver.Chrome()
    for ticker in ticker_list:
        url = "https://hk.finance.yahoo.com/quote/{}.HK/history?p={}.HK".format(ticker, ticker)
        driver.get(url)

        table = driver.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody')
        rows = table.text.split("\n")
        data = []
        for row in rows:
            data.append(row.split(" "))
        header = ["Date", "Open", "High","Low", "Close", "Adj Close", "Volume"]
        df = pd.DataFrame(data, columns = header)

        df.to_excel("data/{}.xlsx".format(ticker), index=None)
        print("{} Done!".format(ticker))

if __name__ == "__main__":
    greeting()
    mode = ask_scrap_mode()
    if mode == 1:
        get_specific()

    elif mode == 2:
        get_all()

    print("Done, piece of cake. Call me when you need me again")
    time.sleep(5)
