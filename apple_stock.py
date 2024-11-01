# apple_stock.py
# This script scrapes Yahoo Finance for Apple's historical stock data (date and close price)
# Source URL: https://finance.yahoo.com/quote/AAPL/history?p=AAPL

import requests
from bs4 import BeautifulSoup

# Yahoo Finance URL for Apple's historical stock data
url = 'https://finance.yahoo.com/quote/AAPL/history?p=AAPL'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table containing historical data
rows = soup.select('table tbody tr')  # Adjust if necessary

print("Apple Stock Data (Date and Close Price):")
for row in rows:
    columns = row.find_all('td')
    if len(columns) > 5:  # Ensure the row contains valid data
        date = columns[0].text.strip()
        close_price = columns[4].text.strip()  # Usually the fifth column for close price
        print(f"Date: {date}, Close Price: {close_price}")
