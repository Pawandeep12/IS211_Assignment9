# american_dishes.py
import requests
from bs4 import BeautifulSoup

# URL to scrape for American dishes popularity
url = "https://today.yougov.com/ratings/consumer/popularity/american-dishes/all"

# Set a user-agent header to avoid being blocked
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Send a request to the website
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the table containing the popularity ratings
    table = soup.find('table')

    # Check if the table was found
    if table:
        # Extract dish data
        dishes = []
        for row in table.find_all('tr')[1:]:  # Skip the header row
            cols = row.find_all('td')
            if len(cols) > 0:
                dish_data = {
                    'Dish': cols[0].text.strip(),
                    'Popularity': cols[1].text.strip(),
                    'Sample Size': cols[2].text.strip(),
                    'Last Updated': cols[3].text.strip()
                }
                dishes.append(dish_data)

        # Output the dish popularity data
        for dish in dishes:
            print(f"{dish['Dish']} - Popularity: {dish['Popularity']}, Sample Size: {dish['Sample Size']}, Last Updated: {dish['Last Updated']}")
    else:
        print("Could not find the dishes popularity table.")
else:
    print(f"Failed to retrieve data: {response.status_code}")

#https://today.yougov.com/ratings/consumer/popularity/american-dishes/all link I am scraping
