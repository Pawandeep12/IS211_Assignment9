# football_stats.py
import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "https://www.cbssports.com/nfl/stats/leaders/touchdowns/"

# Send a request to the website
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table containing player statistics
table = soup.find('table', class_='TableBase-table')

# Extract player data
players = []
for row in table.find_all('tr')[1:21]:  # Get the top 20 players
    cols = row.find_all('td')
    if len(cols) > 0:
        player_data = {
            'Player': cols[1].text.strip(),
            'Position': cols[2].text.strip(),
            'Team': cols[3].text.strip(),
            'Touchdowns': cols[4].text.strip(),
        }
        players.append(player_data)

# Output the player statistics
for player in players:
    print(f"{player['Player']} ({player['Position']}, {player['Team']}): {player['Touchdowns']} TDs")

# Note: Ensure that the website's structure hasn't changed as it may affect scraping.

