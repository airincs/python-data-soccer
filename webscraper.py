import requests
from bs4 import BeautifulSoup
import pandas as pd

def column_extractor(list, keyword, soup):
  """Takes a soup, list, and keyword and returns a list of extracted data"""
  for element in soup.find_all('td', {"data-stat": keyword}):
    list.append(element.text)
  return list

def table_extractor(url, all_lists, keyword_list):
  """Takes a fbref.com URL and creates a DF from the given year/statistics"""
  r = requests.get(url)
  soup = BeautifulSoup(r.content, 'html5lib')
  for list, keyword in zip(all_lists, keyword_list):
    column_extractor(list, keyword, soup)
  df = pd.DataFrame(all_lists)
  df = df.T
  df.columns = keyword_list
  return df
  
wins, draws, losses, goals_for, goals_against, points_avg = ([] for i in range(6))
all_lists = (wins, draws, losses, goals_for, goals_against, points_avg)
keyword_list = ["wins", "draws", "losses", "goals_for", "goals_against", "points_avg"]
url = "https://fbref.com/en/comps/9/Premier-League-Stats"
overall_20_21 = table_extractor(url, all_lists, keyword_list)
print(overall_20_21)