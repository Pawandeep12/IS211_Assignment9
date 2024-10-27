# apple_stock.py
import requests
from bs4 import BeautifulSoup

# URL for Apple stock history
url = "https://finance.yahoo.com/quote/AAPL/history?p=AAPL"

# Request page content
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Find the table of historical data
table = soup.find("table", class_="W(100%) M(0)")
if table:
    rows = table.find_all("tr")[1:]  # Skip header row

    # Display header
    print(f"{'Date':<15} {'Close Price':<10}")
    print("-" * 30)
    
    # Iterate and print rows
    for row in rows:
        columns = row.find_all("td")
        if len(columns) >= 5:  # Check for date and close price columns
            date = columns[0].text.strip()
            close_price = columns[4].text.strip()
            print(f"{date:<15} {close_price:<10}")
else:
    print("Table not found. Page structure may have changed.")
