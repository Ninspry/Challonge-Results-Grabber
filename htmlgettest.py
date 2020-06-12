from bs4 import BeautifulSoup
import requests
import csv

address = 'https://challonge.com/UoYUltimate39'

csv_file = open('bracket.csv', 'w')

csv_writer = csv.writer(csv_file)

csv_writer.writerow(['Players'])

print("Bracket: {0}".format(address))

#Add headers so the website doesn't think we're a bot
headers = requests.utils.default_headers()

headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})

#get the html code for the given page
source = requests.get(address, headers=headers).text

soup = BeautifulSoup(source, 'html5lib')

#challonge name their classes weirdly
numPlayersString = soup.find('div', class_='text')

#convert the value to an integer so we know how many players there are
numberOfPlayers = int(numPlayersString.text.replace(" Players", ""))

print("Number of Attendees: {0}".format(numberOfPlayers))

players = []

rankings = soup.find('div', class_='highlighted')

#find the players and split them into individual items
players = [str(player).split("<br/>") for player in rankings.find_all('strong')]

#the previous line makes the array 2d, this changes it back
players = [i for sublist in players for i in sublist]

#removing the html headers
players = [i.replace("<strong>", "").replace("</strong>", "") for i in players]

for i in range(len(players)):
    csv_writer.writerow([players[i]])

csv_writer.writerow(['Number of Attendees:', numberOfPlayers])

csv_file.close()

print(players)
