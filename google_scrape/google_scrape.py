# PepnoScrape
import sys
import requests
from bs4 import BeautifulSoup

def makeUrl(keyword):
    replaced = keyword.replace(" ", "+")
    return("https://www.google.com/search?client=firefox-b-d&q=" + replaced)

def strip(striptext):
	return striptext.replace('Dochter','').replace('Moeder','').replace('Vader','').replace('Zoon','')
#def getsoup():
# get commandline question and search in google
url = makeUrl(sys.argv[1])
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, 'lxml')
	#return soup

# first result
result = soup.find('div', class_='Z0LcW')

multiple = False
if "are" in sys.argv[1]:
	multiple = True
# if "are" in the question extract list
if result == None:
	if multiple == True:
		for foo in soup.find_all('div', attrs={'class': 'lzmqLb'}):
			if foo.find('div', attrs={'class': 'wfg6Pb'}):
				print(strip(foo.text))
		for foo in soup.find_all('div', attrs={'class': 'IAznY'}):
			if foo.find('div', attrs={'class': 'title'}):
				print(strip(foo.text))
	elif multiple == False:
		result = soup.find('div', class_='title')
if result == None:
	result = soup.find('div', class_='RJn8N xXEKkb ellip')
if result == None:
	result = soup.find(class_='LGOjhe')
if result == None:
	result = soup.find('h3', class_='bNg8Rb').parent.find("span")
if result == None:
	result = soup.find('h3', class_='LC20lb') # wikipedia


#print(soup.find('div', class_='wfg6Pb').text)
#print(soup.find_all(class_='title'))"IAznY" > "title"
if multiple == False:
	print(result.text)
