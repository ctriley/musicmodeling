import re
import csv
import wikipedia
import requests
from BeautifulSoup import BeautifulSoup

def getURL(page):
    """

    :param page: html of web page (here: Python home page) 
    :return: urls in that page 
    """
    start_link = page.find("a href")
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1: end_quote]
    print url
    return url, end_quote

def getURLList(startURL):
	urlList = []
	response = requests.get(startURL)
	# parse html
	print startURL
	print response
	page = str(BeautifulSoup(response.content))
	print page
	while True:
		url, n = getURL(page)
    	print url
    	page = page[n:]
    	if url:
    		urlList.append(url)
    	else:
    		print "did nothing"
    		return urlList


with open('data.csv', 'rb') as f:
	reader = csv.reader(f)
	songlist = list(reader)

expr = re.compile('class="min">(\d)*</span>:<span class="s">(\d)+')

year = "1980"
beginpage = "Billboard Year-End Hot 100 singles of " + str(year)
yearmap = {}
j = 0;
for i in range(1980, 2010):
	yearmap[str(i)] = j
	j = j + 100

wikipage = wikipedia.page(beginpage)
starturl = wikipage.url
getURLList(starturl)

startRange = yearmap[year]
endRange = startRange + 100

for i in range(0, endRange):
	songname = songlist[i][1]
	for songpage in wikipage.links:
		print songpage
		print songname

# needs fixing
# have list of urls, have list of songs
# from url, get title, check against list of songs
# if match, parse page for song length
#for i from 0 to endRange:
#	songname = songlist[i][1]
#	for songpage in wikipage.links:
#		print songpage
#		print songname
#		if(songpage == songname):
#			url = songpage.geturl()			# need to figure out how to get the url for each page
#			print url
#			resp = requests.get(url, params={'action': 'raw'})
#			page = resp.text
#			for line in page.splitlines():
#				if line.startswith('| Length'):
#					length = line.partition('=')[-1].strip()
#					break
#			print length