import json
from bs4 import BeautifulSoup
import requests
with open('playerData.json') as json_data:
    jsonData = json.load(json_data)
    homeStarters=[]
    for i in range(0,5):
    	homeStarters.append(jsonData[i])
    print homeStarters
    awayStarters=[]
    for i in range(15,20):
    	awayStarters.append(jsonData[i])
    print awayStarters

