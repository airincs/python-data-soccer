import requests
from bs4 import BeautifulSoup
import pandas as pd

def column_extractor(list, keyword):
  """Takes a list and fills it with the string keyword found on fbref.com"""
  for element in soup.find_all('td', {"data-stat": keyword}):
    list.append(element.text)
  return list

URL = "https://fbref.com/en/comps/9/Premier-League-Stats"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

wins = []
#for element in soup.find_all('td', {"data-stat": "wins"}):
#  wins.append(element.text)
  
win_column = column_extractor(wins, "wins")
print(win_column)