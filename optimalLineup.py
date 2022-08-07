from bs4 import BeautifulSoup
from operator import attrgetter
import requests

class Player:
    def __init__(self, name = None, obp = None, ops = None, slg = None):
      self.name = name
      self.obp = obp
      self.ops = ops
      self.slg = slg

#Instantiate Player Objects
p1 = Player()
p2 = Player()
p3 = Player()
p4 = Player()
p5 = Player()
p6 = Player()
p7 = Player()
p8 = Player()
p9 = Player()

players = [p1,p2,p3,p4,p5,p6,p7,p8,p9]

#Automatic Stat Retrieval, to manually input, just set each player's fields specifically below.
#Get Page Source
response = requests.get('https://www.mlb.com/stats/new-york-yankees?playerPool=ALL')
r = response.text
soup = BeautifulSoup(r, 'html.parser')

#Get Names
counter = 0
for i in soup.find_all('a', attrs={'class': "bui-link"}):
    if counter == 9:
        break
    if i.get('aria-label') != None:
        players[counter].name = i.get('aria-label')
        counter += 1
#Get OBP
counter = 0
for i in soup.find_all('td', attrs={'class': "number-aY5arzrB align-right-3nN_D3xs is-table-pinned-1WfPW2jT", 'data-col': '15'}):
    if counter == 9:
        break
    players[counter].obp = i.text
    counter += 1
#Get OPS
counter = 0
for i in soup.find_all('td', attrs={'class': "selected-1vxxHvFg col-group-end-2UJpJVwW number-aY5arzrB align-right-3nN_D3xs is-table-pinned-1WfPW2jT", 'data-col': '17'}):
    if counter == 9:
        break
    players[counter].ops = i.text
    counter += 1
#Get SLG
counter = 0
for i in soup.find_all('td', attrs={'class': "number-aY5arzrB align-right-3nN_D3xs is-table-pinned-1WfPW2jT", 'data-col': '16'}):
    if counter == 9:
        break
    players[counter].slg = i.text
    counter += 1

"""calculate lineup
order:
    1. Highest OBP
    2. Highest OPS
    3. 2nd Highest SLG
    4. 2nd Highest OPS
    5. Highest SLG
    6. 3rd Highest OPS
    7. 4th Highest OPS
    8. 5th Highest OPS
    9. 6th Highest OPS
priority: 2,4,1,5,3,6,7,8,9
"""
lineup = ['', '', '', '', '', '', '', '', '']

lineup[1] = max(players, key=attrgetter('ops'))#find player with highest ops
players.remove(lineup[1])#remove player from players list

lineup[3] = max(players, key=attrgetter('ops'))
players.remove(lineup[3])

lineup[0] = max(players, key=attrgetter('obp'))
players.remove(lineup[0])

lineup[4] = max(players, key=attrgetter('slg'))
players.remove(lineup[4])

lineup[2] = max(players, key=attrgetter('slg'))
players.remove(lineup[2])

lineup[5] = max(players, key=attrgetter('ops'))
players.remove(lineup[5])

lineup[6] = max(players, key=attrgetter('ops'))
players.remove(lineup[6])

lineup[7] = max(players, key=attrgetter('ops'))
players.remove(lineup[7])

lineup[8] = max(players, key=attrgetter('ops'))
players.remove(lineup[8])

for n, player in enumerate(lineup):
    print(str(n+1) + '. ' + player.name)
