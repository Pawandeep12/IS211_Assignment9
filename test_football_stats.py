# football_stats.py
import requests
from bs4 import BeautifulSoup

def parse_football_stats():
    url = 'https://www.cbssports.com/nfl/stats/player/scoring/nfl/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    players = []
    for player in soup.select('table tbody tr')[:20]:  # Replace with actual selectors
        name = player.select_one('.PlayerName').text.strip()
        position = player.select_one('.Position').text.strip()
        team = player.select_one('.TeamName').text.strip()
        touchdowns = player.select_one('.Touchdowns').text.strip()
        players.append({
            "name": name,
            "position": position,
            "team": team,
            "touchdowns": touchdowns
        })
    return players

if __name__ == "__main__":
    results = parse_football_stats()
    for player in results:
        print(f"Player: {player['name']}, Position: {player['position']}, Team: {player['team']}, Touchdowns: {player['touchdowns']}")
