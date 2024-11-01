# apple_stock.py
import requests
import yfinance as yf

#Get Apple stock data using yfinance 

date = yf.download("AAPL", start="2023-01-01", end="2023-12-31")

#Display close prices and dates
for date, row in data.ubterrows():
  print(f"Date: {date.date()}, Close Price: {row['Close']")
from bs4 import BeautifulSoup

# URL to scrape for Apple stock data
url = "https://finance.yahoo.com/quote/AAPL/history?p=AAPL"

# Set a user-agent header to avoid being blocked
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Send a request to the website
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the table containing historical stock data
    table = soup.find('table', class_='W(100%) M(0)')

    # Check if the table was found
    if table:
        # Extract historical price data
        stock_data = []
        for row in table.find_all('tr')[1:]:  # Skip the header row
            cols = row.find_all('td')
            if len(cols) > 0:
                date = cols[0].text.strip()
                close_price = cols[4].text.strip()
                stock_data.append({'Date': date, 'Close Price': close_price})

        # Output the stock data
        for data in stock_data:
            print(f"Date: {data['Date']}, Close Price: {data['Close Price']}")
    else:
        print("Could not find the stock data table.")
else:
    print(f"Failed to retrieve data: {response.status_code}")

