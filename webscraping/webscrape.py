from pymongo import MongoClient
import pprint

import pandas as pd

# Requests sends and recieves HTTP requests.
import requests

# Beautiful Soup parses HTML documents in python.
from bs4 import BeautifulSoup

import json
import time

#Create dictionary to store key/value pairs for teams & roster webpage
roster_urls = {}
roster_urls['unc'] = 'https://goheels.com/sports/womens-basketball/roster/'
roster_urls['duke'] = 'https://goduke.com/sports/womens-basketball/roster/'
roster_urls['miami'] = 'https://hurricanesports.com/sports/womens-basketball/roster/'
roster_urls['nc_state'] = 'https://gopack.com/sports/womens-basketball/roster/'

#List of desired seasons of data - will combine with roster_urls to scrape
seasons = ['2009-10', '2010-11', '2011-12', '2017-18', '2018-19', '2019-20']

#Scrape from each webpage and store in MongoDB
client = MongoClient('localhost', 27017)
db = client.wbb
rosters = db.rosters


r = requests.get()
rosters.insert_one({'team': team,
                    'season': season,
                    'html': r.content})

#Pull data from MongoDB and parse with BeautifulSoup

