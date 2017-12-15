import urllib
import urllib.request
from bs4 import BeautifulSoup 

twURL = "https://twitter.com/realDonaldTrump"
twPage = urllib.request.urlopen(twURL)

soup = BeautifulSoup(twPage, "html.parser")

print(soup.title.text)

"""
for link in soup.find_all('a'):
    print(link.get('href'))
    print(link.text)
"""

print(soup.find('div',{"class":"ProfileHeaderCard"}).find('p').text)

i = 1
for tweets in soup.findAll('div',{"class":"content"}):
    print(i)
    print(tweets.find('p').text)
    i = i+1
