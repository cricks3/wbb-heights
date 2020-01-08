from pymongo import MongoClient
import pprint

import pandas as pd

# Beautiful Soup parses HTML documents in python.
from bs4 import BeautifulSoup


#Connect to MongoDB and pull data
client = MongoClient('localhost', 27017)
db = client.wbb
rosters = db.rosters
cursor = rosters.find({})

#HTML from duke website & 2017-2020 have different class tags than 2009-12
#Two conditionals to parse through code
seasons_2 = ['2017-18', '2018-19', '2019-20']
all_teams = []
for item in cursor:
    if item['season'] in seasons_2 or item['team'] == 'duke':
        soup = BeautifulSoup(item['html'], 'html.parser')
        #run parsing code
        heights = [item.text for item in soup.find_all(class_='height')]
        names = [item.text for item in soup.find_all(class_='sidearm-table-player-name')]
        positions = [item.text for item in soup.find_all(class_='rp_position_short')]
        class_yr = [item.text for item in soup.find_all(class_='roster_class')]
        
        #convert heights of string of ft-inches to an integer of inches
        fix_heights = []
        for height in heights:
            fix_heights.append(12*int(height[0]) + int(height[2:]))
        heights = fix_heights
        
        #code to only keep characters relating to positions
        fixed_pos = []
        for string in positions:
                new_pos = [letter for letter in string if letter.isupper()]
                if len(new_pos) == 1:
                    fixed_pos.append(new_pos[0])
                else:
                    fixed_pos.append(new_pos[0] + "/" + new_pos[1])
        positions = fixed_pos
            
        all_teams.append({'team': item['team'],
                          'season': item['season'],
                          'heights': heights,
                          'names': names,
                          'positions': positions,
                          'class_yr': class_yr})
    else:
        soup = BeautifulSoup(item['html'], 'html.parser')
        #run parsing code
        heights = [item.text for item in soup.find_all(class_='sidearm-roster-player-height')]
        first_names = [item.text for item in soup.find_all(class_='sidearm-roster-player-first-name')]
        last_names = [item.text for item in soup.find_all(class_='sidearm-roster-player-last-name')]
        positions = [item.text for item in soup.find_all(class_='sidearm-list-card-details-item sidearm-roster-player-position-short')]
        class_yr = [item.text for item in soup.find_all(class_='sidearm-roster-player-academic-year')]
        
        #code to get first & last names
        names = [item[0] + ' ' + item[1] for item in zip(first_names, last_names)]
        
        #removes duplicate heights
        heights = heights[:len(names)]
        
        #standardize height format
        heights = [item.replace("'","-") for item in heights]
        heights = [item.replace('"', "") for item in heights]
        
        #convert heights of string of ft-inches to an integer of inches
        fix_heights = []
        for height in heights:
            fix_heights.append(12*int(height[0]) + int(height[2:]))
        heights = fix_heights
        
        #remove duplicate class years
        class_yr = class_yr[-len(names):]
        
        #code to only keep characters relating to positions
        fixed_pos = []
        for string in positions:
                new_pos = [letter for letter in string if letter.isupper()]
                if len(new_pos) == 1:
                    fixed_pos.append(new_pos[0])
                else:
                    fixed_pos.append(new_pos[0] + "/" + new_pos[1])
        positions = fixed_pos
    
        #append desired fields to all_teams list
        all_teams.append({'team': item['team'],
                          'season': item['season'],
                          'heights': heights,
                          'names': names,
                          'positions': positions,
                          'class_yr': class_yr})

#check for blank teams and the indexes that contain them
blank_teams = []
blank_indices = []
i=0
for item in all_teams:
    if item['heights'] == []:
        blank_teams.append({'team': item['team'],
                            'season': item['season']
        })
        blank_indices.append(i)
        i+=1
    else:
        i+=1

