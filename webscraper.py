import requests
from bs4 import BeautifulSoup

URL = "https://fbref.com/en/comps/9/Premier-League-Stats"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

for element in soup.find_all('td', {"data-stat": "wins"}):
  print(element.text)