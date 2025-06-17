import requests
from bs4 import BeautifulSoup

url = 'https://finance.yahoo.com/quote/AAPL'
headers = ({'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'})

# UNEEDED: Function to strip the url to the base url for the Amazon URL
'''
def url_strip():
    backslash_count = 0
    index_count = 0
    for i in url:
        if backslash_count >=6:
            break
        if i == '/':
            backslash_count += 1
        index_count += 1
    url = url[:index_count]
    return url
'''

def scrape(url, headers):
    response = requests.get(url, headers=headers)
    print(response)
    soup = BeautifulSoup(response.content, 'lxml')
    #class=yf-4vbjci
    title = str(soup.find("h1", attrs={"class":'yf-4vbjci'}).string).strip()
    price = str(soup.find("span", attrs={"data-testid":'qsp-price'}).string).strip()
    print("Title: ", title)
    print("Price: ", price)

scrape(url, headers)