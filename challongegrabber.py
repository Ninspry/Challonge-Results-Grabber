import requests
from bs4 import BeautifulSoup


class ChallongeGrabber:

    """ Initialises the class by grabbing the web page and creating a soup object """
    def __init__(self, url):
        self.url = url
        self.headers = requests.utils.default_headers()

        # Headers so the website won't kick us for being a bot
        self.headers.update({
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
        })

        try:
            self.source = requests.get(self.url, headers=self.headers).text
            self.soup = BeautifulSoup(self.source, 'html5lib')
        except IOError:
            print("Website read failed")
        except TypeError:
            print("Unknown Error")

    """ Returns an integer of the number of players in the given tournament. """
    def get_number_of_players(self):
        try:
            numplayersstring = self.soup.find('div', class_='text')
            numberofplayers = int(numplayersstring.text.replace(" Players", ""))
        except IOError:
            numberofplayers = 0

        return numberofplayers

    """ Returns a list of all players in the given tournament. """
    def get_list_of_players(self):
        players = []
        rankings = self.soup.find('div', class_='highlighted')
        players = [str(player).split("<br/>") for player in rankings.find_all('strong')]
        players = [i for sublist in players for i in sublist]
        players = [player.replace("<strong>", "").replace("</strong>", "") for player in players]
        return players
