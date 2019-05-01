from bs4 import BeautifulSoup
import requests
import json

urlPlays = "http://www.espn.com/nba/playbyplay?gameId=401126819&wsVar=us~nba~gamepackage,desktop,en"
responsePlays = requests.get(urlPlays, timeout=5)
htmlPlays = responsePlays.content
soupPlays = BeautifulSoup(htmlPlays, "lxml")

# Lines 11-28 gets the play by play info
playArray = []
quarters = ["1", "2", "3", "4"] #trying to get the code to loop through all quarters of the game
for quarter in quarters:
    quarterBody = soupPlays.find('div', attrs={"id": "gp-quarter-" + quarter})
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

# Got all players names

urlPlayers = "http://www.espn.com/nba/boxscore?gameId=401126819&wsVar=us~nba~gamepackage,desktop,en"
responsePlayers = requests.get(urlPlayers, timeout=5)
htmlPlayers = responsePlayers.content
soupPlayers = BeautifulSoup(htmlPlayers, "lxml")

playersArray = []
for columnBody in soupPlayers.find('div', attrs={"id": "gamepackage-boxscore-module"}):
    for eachRow in columnBody.findAll('tr'):
        playersObject = {}
        for player in eachRow.findAll('td', attrs={"class": "name"}):
            for playerAbbrev in player.findAll('span', attrs={"class": "abbr"}):
                text = playerAbbrev.text
                playersObject = {"name": text}
                playersArray.append(playersObject)
            with open('playerData.json', 'w') as outfile:
                json.dump(playersArray, outfile)

