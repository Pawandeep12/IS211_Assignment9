import requests
from bs4 import BeautifulSoup

def parse_apple_stock():
    url = 'https://finance.yahoo.com/quote/AAPL/history?p=AAPL'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    stock_data = []
    rows = soup.select('table tbody tr')
    for row in rows:
        columns = row.find_all('td')
        if len(columns) > 5:
            date = columns[0].text.strip()
            close_price = columns[4].text.strip()
            stock_data.append({
                "date": date,
                "close_price": close_price
            })
    return stock_data

if __name__ == "__main__":
    results = parse_apple_stock()
    for data in results:
        print(f"Date: {data['date']}, Close Price: {data['close_price']}")
