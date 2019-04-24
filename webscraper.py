from bs4 import BeautifulSoup
import requests
import json

url = "http://www.espn.com/nba/playbyplay?gameId=401126819"
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")

playArray = []
for play in content.findAll('div', attrs={"id": "gp-quarter-1"}):
    playObject = {
        "timestamp": play.find('td', attrs={"class": "time-stamp"}).text.encode('utf-8'),
        "gameDetails": play.find('td', attrs={"class": "game-details"}).text.encode('utf-8'),
        "combinedScore": play.find('td', attrs={"class": "combined-score"}).text.encode('utf-8'),
    }
    print playObject
    