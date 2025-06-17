import yfinance as yf

from swiftshadow import QuickProxy

#prox = QuickProxy().as_string()
#print("Using Proxy: ", prox)
#yf.set_config(proxy=str(prox))

def getData(symbol, history=False):
    dat = yf.Ticker(symbol)

    # Fetching data index
    print("Stock Symbol: ", dat.info['symbol'])
    print("Company Name: ", dat.info['longName'])
    print("Current Price: ", dat.info['currentPrice'])
    print("Market Cap: ", dat.info['marketCap'])
    print("52 Week High: ", dat.info['fiftyTwoWeekHigh'])
    print("52 Week Low: ", dat.info['fiftyTwoWeekLow'])
    print("PE Ratio: ", dat.info['forwardPE'])
    print("Dividend Yield: ", dat.info['dividendYield'])
    print("Beta: ", dat.info['beta'])
    print("Volume: ", dat.info['volume'])
    print("Average Volume: ", dat.info['averageVolume'])
    print("Previous Close: ", dat.info['regularMarketPreviousClose'])
    print("Open: ", dat.info['regularMarketOpen'])
    print("Day's Range: ", dat.info['regularMarketDayRange'])
    print("Year's Range: ", dat.info['fiftyTwoWeekRange'])
    print("Ex-Dividend Date: ", dat.info['exDividendDate'])
    print("Last Split Date: ", dat.info['lastSplitDate'])
    print("Last Split Factor: ", dat.info['lastSplitFactor'])
    print("Currency: ", dat.info['currency'])
    print("Market State: ", dat.info['marketState'])
    print("Regular Market Time: ", dat.info['regularMarketTime'])
    print("Quote Type: ", dat.info['quoteType'])
    print("Price Change: ", dat.info['regularMarketChange'])
    print("Price Change Percent: ", dat.info['regularMarketChangePercent'])
    print("Price Change Percentage: ", dat.info['regularMarketChangePercent'])
    print("Price Change Percentage (raw): ", dat.info['regularMarketChangeRaw'])
    print("Price Change Percentage (formatted): ", dat.info['regularMarketChangePercentFormatted'])

    if history:
        # Fetching historical data
        hist = dat.history(period=history)
        print("\nHistorical Data (last {}):".format(history))
        print(hist)

getData('AAPL', history='1y')  # Example usage with 1 year of historical data