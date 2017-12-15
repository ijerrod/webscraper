import urllib
import urllib.request
from bs4 import BeautifulSoup
import os

def make_soup(url):
    webpage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(webpage, "html.parser")
    return soupdata

playerdatasaved = ""
soup = make_soup("https://www.basketball-reference.com/players/a/")

for record in soup.findAll('tr'):
    playerdata = ""
    for data in record.findAll('td'):
        playerdata = playerdata + "," + data.text
    if len(playerdata) != 0:
        playerdatasaved = playerdatasaved + "\n" + playerdata[1:]

header = "Player, From, To, Pos, Ht, Wt, Birth Date, College"
file = open(os.path.expanduser("Basketball.csv"), "wb")
file.write(bytes(header, encoding = "ascii", errors = "ignore"))
file.write(bytes(playerdatasaved, encoding="ascii", errors = "ignore"))

print(playerdatasaved)