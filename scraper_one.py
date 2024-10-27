# football_stats.py
import requests
from bs4 import BeautifulSoup

# URL for CBS NFL stats page - touchdowns
url = "https://www.cbssports.com/nfl/stats/leaders/live/touchdowns/regular"

# Request page content
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Find the touchdowns table
table = soup.find("table", class_="TableBase-table")
if table:
    rows = table.find_all("tr")[1:21]  # Skipping header row and selecting top 20 players

    # Printing the header
    print(f"{'Player':<20} {'Position':<10} {'Team':<10} {'Touchdowns':<5}")
    print("-" * 50)
    # Iterating over rows
    for row in rows:
        columns = row.find_all("td")
        player = columns[0].text.strip()
        position = columns[1].text.strip()
        team = columns[2].text.strip()
        touchdowns = columns[3].text.strip()
        print(f"{player:<20} {position:<10} {team:<10} {touchdowns:<5}")
else:
    print("Table not found or page structure may have changed.")
