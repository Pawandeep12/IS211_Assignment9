# apple_stock.py
import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "https://finance.yahoo.com/quote/AAPL/history?p=AAPL"

# Send a request to the website
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table containing historical stock data
table = soup.find('table', class_='W(100%) M(0)')

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

# Note: Ensure that the website's structure hasn't changed as it may affect scraping.
