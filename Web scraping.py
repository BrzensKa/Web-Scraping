# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

file = open('test.md' , 'w+')

# Set the URL you want to webscrape from
url = 'https://en.wikipedia.org/wiki/Dota_2'
source =urllib.request.urlopen(url)

# Parse HTML and save to BeautifulSoup object¶
soup = BeautifulSoup(source, "html.parser")

table = soup.find('table' , { 'class' : 'hproduct' })
table_rows = table.find_all('tr')

for row in table_rows:
    if row.find('th') == None: continue
    file.write('- ' + row.find('th').getText() + '\n')
    
    for item in row.find_all('td'):
        file.write('    - ' + item.getText() + '\n')

file.close()
