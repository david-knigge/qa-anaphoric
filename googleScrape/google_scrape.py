# PepnoScrape
import sys
import requests
from bs4 import BeautifulSoup

def makeUrl(keyword):
    replaced = keyword.replace(" ", "+")
    return("https://www.google.com/search?client=firefox-b-d&q=" + replaced)

url = makeUrl(sys.argv[1])
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, 'lxml')
result = soup.find('div', class_='Z0LcW')


if result == None:
    result = soup.find('div', class_='title')
if result == None:
    result = soup.find('div', class_='RJn8N xXEKkb ellip')
if result == None:
    result = soup.find(class_='LGOjhe')
if result == None:
    result = soup.find('h3', class_='LC20lb') # wikipedia

print(result.text)
