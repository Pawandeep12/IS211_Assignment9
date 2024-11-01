import requests
from bs4 import BeautifulSoup

#THE LINK I AM SCRAPING 
url = "https://en.wikipedia.org/wiki/List_of_Walt_Disney_Animation_Studios_films"


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}


response = requests.get(url, headers=headers)


if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

   
    table = soup.find('table', class_='wikitable')

    
    if table:
        films = []
        for row in table.find_all('tr')[1:]:  
            cols = row.find_all('td')
            if len(cols) >= 3: 
                title = cols[0].text.strip()
                release_year = cols[1].text.strip()
                director = cols[2].text.strip()
                films.append({'Title': title, 'Release Year': release_year, 'Director': director})

      
        for film in films:
            print(f"Title: {film['Title']}, Release Year: {film['Release Year']}, Director: {film['Director']}")
    else:
        print("Could not find the Disney films table.")
else:
    print(f"Failed to retrieve data: {response.status_code}")


