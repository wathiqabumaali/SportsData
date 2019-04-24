from bs4 import BeautifulSoup
import requests
import json

url = "http://www.espn.com/nba/playbyplay?gameId=401126819"
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")

playArray = []
quarters = ["1", "2", "3", "4"] #trying to get the code to loop through all quarters of the game
for i in range(len(quarters)):
	for play in content.findAll('div', attrs={"id": "gp-quarter-" + str(i)}):
	    playObject = {
	        "timestamp": play.find('td', attrs={"class": "time-stamp"}).text.encode('utf-8'),
	        "gameDetails": play.find('td', attrs={"class": "game-details"}).text.encode('utf-8'),
	        "combinedScore": play.find('td', attrs={"class": "combined-score"}).text.encode('utf-8'),
	    }
	    playArray.append(playObject)
	with open('playData.json', 'w') as outfile:
	    json.dump(playArray, outfile)

    