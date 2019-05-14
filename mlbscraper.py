"""
Written by Trevor Walker

This python file will scrape the mlb site once every week in order
to have the most recent baseball leaders and statistics to look at.
It uses the Beautiful Soup library to process the html data, and get
the table of stats from mlb.com

make sure you pip install the library before execution, directions
are in the link below.

https://pypi.org/project/beautifulsoup4/

https://www.mlb.com

"""
import json
import os
from bs4 import BeautifulSoup
import requests

URL = "http://m.mlb.com/stats/"
DATA = requests.get(URL)
SOUP = BeautifulSoup(DATA.text, 'html.parser')

TABLE = SOUP.find('table', {'class':'stats_table data hitting js-accessible'})
TBODY = TABLE.find('tbody')
THEAD = TABLE.find('thead')

def populate_dictionary():
    """
    this function creates a dictionary of dictionaries that
    will later be exported to a json file. It uses the table
    found in on the stats URL listed above. After finding the
    tr values, it creates another dictionary using the player's
    name as the key. That player's dictionary values are their
    stats.
    """
    my_dictionary = {}
    for tr_ in TBODY.find_all('tr'):
        name = tr_.find_all('td')[1].text.strip()
        my_dictionary[name] = {}
        for i in range(34):
            if i > 5:
                element = THEAD.find_all('th')[i].text.strip()
                my_dictionary[name][element] = float(tr_.find_all('td')[i].text.strip())
    return my_dictionary


def order(my_dictionary, stat):
    """
    this function takes in a dictionary and statistic, and orders
    the players by name and stat from biggest to smallest. The first
    player in the 0th index of the returned list is the league leader
    for that stat. The list size is 50 players.
    """
    player_list = []
    for player in my_dictionary:
        if my_dictionary[player]['AB'] > 50:
            player_stat = my_dictionary[player][stat]
            player_list.append([player, player_stat])
    best_players = sorted(player_list, key=lambda tup: tup[1], reverse=True)
    return best_players


if __name__ == '__main__':
    STATS = populate_dictionary()

    NEWJSON = json.dumps(STATS)
    NEWFILE = open("currentStats.json", "w")
    NEWFILE.write(NEWJSON)
    NEWFILE.close()

    EXISTS = os.path.isfile("prevStats.json")
    if not EXISTS:
        ADDJSON = open("prevStats.json", "w")
        ADDJSON.write(NEWJSON)
        ADDJSON.close()

    with open('prevStats.json') as json_file:
        DATA1 = json.load(json_file)
    with open('currentStats.json') as json_file:
        DATA2 = json.load(json_file)

    NEWDATA1 = order(DATA1, 'AVG')
    NEWDATA2 = order(DATA2, 'AVG')

    if NEWDATA1 == NEWDATA2:
        os.remove("currentStats.json")
    else:
        os.remove("prevStats.json")
        os.rename("currentStats.json", "prevStats.json")
