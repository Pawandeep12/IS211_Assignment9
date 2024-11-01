# football_stats.py
# This script scrapes the CBS NFL stats page for league leaders in touchdowns
# Source URL: https://www.cbssports.com/nfl/stats/player/scoring/nfl/

import requests
from bs4 import BeautifulSoup

# URL for CBS NFL stats page
url = 'https://www.cbssports.com/nfl/stats/player/scoring/nfl/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Example parsing - adjust selectors based on actual page structure
players = soup.select('table tbody tr')  # Update selector based on actual HTML structure

print("Top 20 NFL Players by Touchdowns:")
for player in players[:20]:
    name = player.select_one('.PlayerName').text.strip()  # Adjust selector
    position = player.select_one('.Position').text.strip()  # Adjust selector
    team = player.select_one('.TeamName').text.strip()  # Adjust selector
    touchdowns = player.select_one('.Touchdowns').text.strip()  # Adjust selector
    
    print(f"Player: {name}, Position: {position}, Team: {team}, Touchdowns: {touchdowns}")
