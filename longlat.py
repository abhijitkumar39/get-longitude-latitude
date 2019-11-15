import requests
import json
from bs4 import BeautifulSoup

place=input("Enter the place : ")
MapUrl="https://www.google.com/search?tbm=map&q={}".format(place)
response =requests.get(MapUrl)
response=response.text[4:]
coordinatesData=json.loads(response)
cordinates=coordinatesData[1][0]
longitude=cordinates[1]
latitude=cordinates[2]

print('longitude---> ',longitude," latitude--->",latitude)