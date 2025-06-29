import yfinance as yf
from swiftshadow import QuickProxy
from tabulate import tabulate
import pandas as pd

#prox = QuickProxy().as_string()
#print("Using Proxy: ", prox)
#yf.set_config(proxy=str(prox))

'''
def getData(symbol, history=False):
    symbol = str(symbol).upper()
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
    print("Short Ratio: ", dat.info['shortRatio'])
    print("Short Percent of Float: ", dat.info['shortPercentOfFloat'])
    print("Forward PE Ratio: ", dat.info['forwardPE'])
    print("Trailing PE Ratio: ", dat.info['trailingPE'])
    print("Price to Book Ratio: ", dat.info['priceToBook'])
    print("Price to Sales Ratio: ", dat.info['priceToSalesTrailing12Months'])
    print("EBITDA: ", dat.info['ebitda'])
    print("Gross Profits: ", dat.info['grossProfits'])
    print("Operating Cash Flow: ", dat.info['operatingCashflow'])
    print("Free Cash Flow: ", dat.info['freeCashflow'])
    print("Total Cash: ", dat.info['totalCash'])
    print("Total Debt: ", dat.info['totalDebt'])
    print("Return on Equity: ", dat.info['returnOnEquity'])
    print("Return on Assets: ", dat.info['returnOnAssets'])
    # print("Return on Investment: ", dat.info['returnOnInvestment'])
    print("Operating Margin: ", dat.info['operatingMargins'])
    print("Profit Margin: ", dat.info['profitMargins'])
    print("Revenue: ", dat.info['totalRevenue'])
    print("Revenue Growth: ", dat.info['revenueGrowth'])
    print("Net Income: ", dat.info['netIncomeToCommon'])

    """
    print("Total Assets: ", dat.info['totalAssets'])
    print("Total Liabilities: ", dat.info['totalLiab'])
    print("Cash and Cash Equivalents: ", dat.info['cash'])
    print("Cash per Share: ", dat.info['cashPerShare'])
    print("Book Value per Share: ", dat.info['bookValue'])
    print("Shares Outstanding: ", dat.info['sharesOutstanding'])
    print("Shares Float: ", dat.info['floatShares'])
    print("Institutional Ownership: ", dat.info['heldPercentInstitutions'])
    print("Insider Ownership: ", dat.info['heldPercentInsiders'])
    print("Analyst Recommendations: ", dat.recommendations)
    print("Analyst Price Target: ", dat.info['targetMeanPrice'])
    print("Analyst Price Target High: ", dat.info['targetHighPrice'])
    print("Analyst Price Target Low: ", dat.info['targetLowPrice'])
    print("Analyst Price Target Standard Deviation: ", dat.info['targetMedianPrice'])
    print("Analyst Price Target Number of Analysts: ", dat.info['numberOfAnalystOpinions'])
    print("Sector: ", dat.info['sector'])
    print("Industry: ", dat.info['industry'])
    print("Website: ", dat.info['website'])
    print("Address: ", dat.info['address1'])
    print("Phone: ", dat.info['phone'])
    print("Description: ", dat.info['longBusinessSummary'])
    print("Last Updated: ", dat.info['lastUpdateTime'])
    print("Time Zone: ", dat.info['timeZone'])
    print("Time Zone Name: ", dat.info['timeZoneName'])
    """

    if history:
        # Fetching historical data
        #print as nice table using python library tabulate
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', 1000)
        from datetime import datetime, timedelta
        if history == '1d':
            history = '1d'
        elif history == '1w':
            history = '1w'
        elif history == '1m':
            history = '1mo'
        elif history == '3m':
            history = '3mo'
        elif history == '6m':
            history = '6mo'
        elif history == '1y':
            history = '1y'
        elif history == '2y':
            history = '2y'
        elif history == '5y':
            history = '5y'
        else:
            raise ValueError("Invalid history period. Use: 1d, 1w, 1m, 3m, 6m, 1y, 2y, or 5y.")
        if history == '1d':
            hist = dat.history(period='1d', interval='1m')
        else:
            hist = dat.history(period=history)
        
        hist.reset_index(inplace=True)
        hist['Date'] = hist['Date'].dt.strftime('%Y-%m-%d %H:%M:%S')
        hist = hist[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]

        print("\nHistorical Data for the last", history, ":\n")
        print(tabulate(hist, headers='keys', tablefmt='pretty', showindex=False))
        return dat.info
        #return hist
    else:
        print("\nNo historical data requested.\n")
        return dat.info
        #return None
'''
        
import yfinance as yf

def getData(symbol, history=False):
    dat = yf.Ticker(symbol)
    info = dat.info

    hist = None
    if history:
        # Accept common history periods; default 1mo if history is truthy but not specific
        valid_periods = ['1d', '1wk', '1mo', '3mo', '6mo', '1y', '2y', '5y']
        period = history if history in valid_periods else '1mo'

        hist_df = dat.history(period=period)
        hist_df.reset_index(inplace=True)
        # Format date nicely
        hist_df['Date'] = hist_df['Date'].dt.strftime('%Y-%m-%d')
        # Convert DataFrame to list of dicts for easy Jinja rendering
        hist = hist_df.to_dict(orient='records')

    return {'info': info, 'history': hist}