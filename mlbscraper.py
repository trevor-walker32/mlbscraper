from bs4 import BeautifulSoup
import time
import requests

sketchURL = "http://m.mlb.com/stats/"
realURL = "http://mlb.mlb.com/stats/sortable.jsp#elem=%5Bobject+Object%5D&tab_level=child&click_text=Sortable+Player+hitting&game_type='R'&season=2019&season_type=ANY&league_code='MLB'&sectionType=sp&statType=hitting&page=1&ts=1557199491783"

data = requests.get(sketchURL)
soup = BeautifulSoup(data.text, 'html.parser')

table = soup.find('table',{'class':'stats_table data hitting js-accessible'})
tbody = table.find('tbody')
thead = table.find('thead')

def populateDictionary():
    myDictionary = {}
    for tr in tbody.find_all('tr'):
        name = tr.find_all('td')[1].text.strip()
        myDictionary[name] = {}
        for i in range(34):
            if i > 5:
                element = thead.find_all('th')[i].text.strip()
                myDictionary[name][element] = tr.find_all('td')[i].text.strip()
    return myDictionary

if __name__ == '__main__':
    dict = populateDictionary()
    print(dict)

    
