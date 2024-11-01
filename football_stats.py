import requests
from bs4 import BeautifulSoup

def parse_football_stats():
    url = 'https://www.cbssports.com/nfl/stats/player/scoring/nfl/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    players = []
    for player in soup.select('table tbody tr')[:20]:  # Replace with actual selectors
        # Adjust these selectors to match the website's structure
        name = player.select_one('.PlayerName').text.strip() if player.select_one('.PlayerName') else 'N/A'
        position = player.select_one('.Position').text.strip() if player.select_one('.Position') else 'N/A'
        team = player.select_one('.TeamName').text.strip() if player.select_one('.TeamName') else 'N/A'
        touchdowns = player.select_one('.Touchdowns').text.strip() if player.select_one('.Touchdowns') else '0'
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
