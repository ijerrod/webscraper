import urllib
import urllib.request
from bs4 import BeautifulSoup

def make_soup(url):
    webpage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(webpage, "html.parser")
    return soupdata

soup = make_soup("https://www.basketball-reference.com/players/a/")

for record in soup.findAll('tr'):
    for data in record.findAll('td'):
        print(data.text)