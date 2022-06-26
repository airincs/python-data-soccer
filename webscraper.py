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

## Gathering 'summary' statistics
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

overall_df = pd.concat([overall_21_22, overall_20_21, overall_19_20])
overall_df.to_csv("overallDF.csv", encoding='utf-8', index=False)


## Gathering 'shooting' statistics
keyword_list = ["goals", "shots_total_per90", "goals_per_shot", "average_shot_distance"]
goals, shots_total_per90, goals_per_shot, average_shot_distance = ([] for i in range(4))
all_lists = (goals, shots_total_per90, goals_per_shot, average_shot_distance)
shooting_21_22 = table_extractor("https://fbref.com/en/comps/9/shooting/Premier-League-Stats", all_lists, keyword_list)
shooting_21_22 = shooting_21_22.iloc[:20]
goals, shots_total_per90, goals_per_shot, average_shot_distance = ([] for i in range(4))
all_lists = (goals, shots_total_per90, goals_per_shot, average_shot_distance)
shooting_20_21 = table_extractor("https://fbref.com/en/comps/9/10728/shooting/2020-2021-Premier-League-Stats", all_lists, keyword_list)
shooting_20_21 = shooting_20_21.iloc[:20]
goals, shots_total_per90, goals_per_shot, average_shot_distance = ([] for i in range(4))
all_lists = (goals, shots_total_per90, goals_per_shot, average_shot_distance)
shooting_19_20 = table_extractor("https://fbref.com/en/comps/9/3232/shooting/2019-2020-Premier-League-Stats", all_lists, keyword_list)
shooting_19_20 = shooting_19_20.iloc[:20]

shooting_df = pd.concat([shooting_21_22, shooting_20_21, shooting_19_20])
shooting_df.to_csv("shootingDF.csv", encoding='utf-8', index=False)

## Gathering 'passing' statistics
keyword_list = ["passes_completed", "passes_pct", "assisted_shots", "passes_completed_short"]
passes_completed, passes_pct, assisted_shots, passes_completed_short = ([] for i in range(4))
all_lists = (passes_completed, passes_pct, assisted_shots, passes_completed_short)
passing_21_22 = table_extractor("https://fbref.com/en/comps/9/passing/Premier-League-Stats", all_lists, keyword_list)
passing_21_22 = passing_21_22.iloc[:20]
passes_completed, passes_pct, assisted_shots, passes_completed_short = ([] for i in range(4))
all_lists = (passes_completed, passes_pct, assisted_shots, passes_completed_short)
passing_20_21 = table_extractor("https://fbref.com/en/comps/9/10728/passing/2020-2021-Premier-League-Stats", all_lists, keyword_list)
passing_20_21 = passing_20_21.iloc[:20]
passes_completed, passes_pct, assisted_shots, passes_completed_short = ([] for i in range(4))
all_lists = (passes_completed, passes_pct, assisted_shots, passes_completed_short)
passing_19_20 = table_extractor("https://fbref.com/en/comps/9/3232/passing/2019-2020-Premier-League-Stats", all_lists, keyword_list)
passing_19_20 = passing_19_20.iloc[:20]

passing_df = pd.concat([passing_21_22, passing_20_21, passing_19_20])
passing_df.to_csv("passingDF.csv", encoding='utf-8', index=False)