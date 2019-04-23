from bs4 import BeautifulSoup
import requests

url = "http://www.espn.com/nba/playbyplay?gameId=401126819"
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")

for play in content.findAll('tr'):
    print play.text.encode('utf-8')
