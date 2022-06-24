import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep

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
 
keyword_list = ["wins", "draws", "losses", "goals_for", "goals_against", "points_avg"] 
wins, draws, losses, goals_for, goals_against, points_avg = ([] for i in range(6))
all_lists = (wins, draws, losses, goals_for, goals_against, points_avg)
overall_21_22 = table_extractor("https://fbref.com/en/comps/9/Premier-League-Stats", all_lists, keyword_list)
wins, draws, losses, goals_for, goals_against, points_avg = ([] for i in range(6))
all_lists = (wins, draws, losses, goals_for, goals_against, points_avg)
overall_20_21 = table_extractor("https://fbref.com/en/comps/9/10728/2020-2021-Premier-League-Stats", all_lists, keyword_list)
wins, draws, losses, goals_for, goals_against, points_avg = ([] for i in range(6))
all_lists = (wins, draws, losses, goals_for, goals_against, points_avg)
overall_19_20 = table_extractor("https://fbref.com/en/comps/9/3232/2019-2020-Premier-League-Stats", all_lists, keyword_list)
wins, draws, losses, goals_for, goals_against, points_avg = ([] for i in range(6))
all_lists = (wins, draws, losses, goals_for, goals_against, points_avg)
overall_18_19 = table_extractor("https://fbref.com/en/comps/9/1889/2018-2019-Premier-League-Stats", all_lists, keyword_list)
sleep(1)
overall_df = pd.concat([overall_21_22, overall_20_21, overall_19_20, overall_18_19])
print(overall_df)