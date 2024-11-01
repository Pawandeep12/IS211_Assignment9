import requests
import yfinance as yf


date = yf.download("AAPL", start="2023-01-01", end="2023-12-31")

for date, row in date.iterrows():
  print(f"Date: {date.date()}, Close Price: {row['Close']}")
from bs4 import BeautifulSoup

url = "https://finance.yahoo.com/quote/AAPL/history?p=AAPL"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')


    table = soup.find('table', class_='W(100%) M(0)')

    if table:
      
        stock_data = []
        for row in table.find_all('tr')[1:]: 
            cols = row.find_all('td')
            if len(cols) > 0:
                date = cols[0].text.strip()
                close_price = cols[4].text.strip()
                stock_data.append({'Date': date, 'Close Price': close_price})

        
        for data in stock_data:
            print(f"Date: {data['Date']}, Close Price: {data['Close Price']}")
    else:
        print("Could not find the stock data table.")
else:
    print(f"Failed to retrieve data: {response.status_code}")

