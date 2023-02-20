from bs4 import BeautifulSoup
from operator import attrgetter
import requests

# Player class
class Player:
    def __init__(self, name = None, obp = None, ops = None, slg = None):
      self.name = name
      self.obp = obp
      self.ops = ops
      self.slg = slg

    def __str__(self):
        return str(self.name) + " OBP: " + str(self.obp) + " OPS: " + str(self.ops) + " SLG: " + str(self.slg)

if __name__ == "__main__":
    # Initialize player list
    players = []

    # Get command line options
    print("Enter 'm' for manual, 'p' for preview, or 'l' to fill from an MLB team page link.")
    options = ['m', 'p', 'l']
    op = input()
    while (op not in options):
        print("Invalid option:", op)
        op = input("Option: ")

    # Parse command line options
    if (op == 'm'):
        n = input("How many players to input? ")
        for i in range(n):
            players[i].name = input("Player " + str(i+1) + " name: ")
            players[i].obp = input(players[i].name + " OBP: ")
            players[i].ops = input(players[i].name + " OPS: ")
            players[i].slg = input(players[i].name + " SLG: ")
    else:
        response = "null"
        if (op == 'l'):
            # Get link from user
            try:
                response = requests.get(input("Enter MLB team page link (Ex. https://www.mlb.com/stats/new-york-yankees?playerPool=ALL): "))
            except:
                print("An error occured while fetching the link.")
                exit()
        else:
            # Load preview link
            response = requests.get('https://www.mlb.com/stats/new-york-yankees?playerPool=ALL')
        
        # Get Page Source
        r = response.text
        soup = BeautifulSoup(r, 'html.parser')
        
        # Column index changes by page. Find column index for each stat.
        OBPcol = "None"
        SLGcol = "None"
        OPScol = "None"
        for i in soup.find_all('th'):
            if ("OBP" in i.text):
                OBPcol = str(i['data-col'])
            elif ("SLG" in i.text):
                SLGcol = str(i['data-col'])
            elif ("OPS" in i.text):
                OPScol = str(i['data-col'])

        # Load names
        for i in soup.find_all('a', attrs={'class': "bui-link"}):
            if i.get('aria-label') != None:
                players.append(Player(name=i.get('aria-label')))
        # Load OBP
        counter = 0
        for i in soup.find_all('td', attrs={'data-col': OBPcol}):
            if counter == len(players):
                break
            players[counter].obp = i.text
            counter += 1
        # Load SLG
        counter = 0
        for i in soup.find_all('td', attrs={'data-col': SLGcol}):
            if counter == len(players):
                break
            players[counter].slg = i.text
            counter += 1
        # Load OPS
        counter = 0
        for i in soup.find_all('td', attrs={'data-col': OPScol}):
            if counter == len(players):
                break
            players[counter].ops = i.text
            counter += 1

    """calculate lineup
    order:
        1. Highest OBP
        2. Highest OPS
        3. Highest SLG
        4. Highest OPS
        5. Highest SLG
        6. Highest OPS
        7. Highest OPS
        8. Highest OPS
        9. Highest OPS
    priority: 2,4,1,5,3,6,7,8,9
    """
    # Create priority tuple
    priority = ((2, "ops"), (4, "ops"), (1, "obp"), (5, "slg"), (3, "slg"), (6, "ops"), (7, "ops"), (8, "ops"), (9, "ops"))
    # Initialize lineup
    lineup = [Player()] * 9

    # Display loaded players
    for i in players:
        print(i)

    # Create lineup
    for i in priority:
        if len(players) == 0:
            break
        lineup[i[0]-1] = max(players, key=attrgetter(i[1]))#find player with highest of chosen stat
        players.remove(lineup[i[0]-1])#remove player from players list   

    # filter out empty slots
    # lineup = [x for x in lineup if x != '']

    # Display lineup
    print("~~~~~~~~~~~~~~~~~~~~~~~~~OPTIMAL LINEUP~~~~~~~~~~~~~~~~~~~~~~~~~")
    for n, player in enumerate(lineup):
        print(str(n+1) + '. ' + str(player.name))
