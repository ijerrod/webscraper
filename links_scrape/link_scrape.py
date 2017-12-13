# Import required modules
from bs4 import BeautifulSoup
import requests
import csv

# Prompt user to enter a URL
url = input("Enter a Website URL to scrape its links: ")

# Opens and reads URL
r = requests.get(url)
data = r.text

# close open session
r.close()

# HTML Parser
soup = BeautifulSoup(data, 'html.parser')

# Set up CSV file
filename = "links.csv"
f = open(filename, "w")
headers = "links\n"
f.write(headers)

# Print each link found
for link in soup.find_all('a'):
    pLink = link.get('href')

    print(pLink)

    f.write(pLink + "\n")

f.close()