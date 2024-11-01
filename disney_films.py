# disney_films.py
import requests
from bs4 import BeautifulSoup

# URL to scrape for Disney theatrical animated feature films
url = "https://en.wikipedia.org/wiki/List_of_Walt_Disney_Animation_Studios_films"

# Set a user-agent header to avoid being blocked
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Send a request to the website
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the table containing the films
    table = soup.find('table', class_='wikitable')

    # Check if the table was found
    if table:
        films = []
        for row in table.find_all('tr')[1:]:  # Skip the header row
            cols = row.find_all('td')
            if len(cols) >= 3:  # Ensure there are enough columns
                title = cols[0].text.strip()
                release_year = cols[1].text.strip()
                director = cols[2].text.strip()
                films.append({'Title': title, 'Release Year': release_year, 'Director': director})

        # Output the film data
        for film in films:
            print(f"Title: {film['Title']}, Release Year: {film['Release Year']}, Director: {film['Director']}")
    else:
        print("Could not find the Disney films table.")
else:
    print(f"Failed to retrieve data: {response.status_code}")


#https://en.wikipedia.org/w/index.php?title=List_of_Disney_theatrical_animated_feature_films&section=2&oldid=1254577488&action=edit--- link I am scraping
