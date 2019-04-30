from bs4 import BeautifulSoup
import requests
import json

url = "http://www.espn.com/nba/playbyplay?gameId=401126819&wsVar=us~nba~gamepackage,desktop,en"
response = requests.get(url, timeout=5)
html = response.content
soup = BeautifulSoup(html, "lxml")

playArray = []
quarters = ["1", "2", "3", "4"] #trying to get the code to loop through all quarters of the game
for quarter in quarters:
    quarterBody = soup.find('div', attrs={"id": "gp-quarter-" + quarter})
    for row in quarterBody.findAll('tr'):
        playObject = {}
        for time in row.findAll('td', attrs={"class": "time-stamp"}):
            text = time.text
            playObject = {"timestamp": text}
        for gameDetails in row.findAll('td', attrs={"class": "game-details"}):
            text = gameDetails.text
            playObject["game-details"] = text
        for combinedScore in row.findAll('td', attrs={"class": "combined-score"}):
            text = combinedScore.text
            playObject["combined-score"] = text
            playArray.append(playObject)
        with open('playData.json', 'w') as outfile:
            json.dump(playArray, outfile)
