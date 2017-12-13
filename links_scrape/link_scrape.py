from bs4 import BeautifulSoup
import requests

url = input("Enter a Website URL to scrape its links: ")

r = requests.get(url)

data = r.text

soup = BeautifulSoup(data, 'html.parser')

linkList = ''

for link in soup.findAll('a'):
    print(link.get('href'))