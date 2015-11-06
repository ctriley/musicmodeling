#byyear2.py

import urllib2
import re
import csv
import wikipedia
import ssl
import urllib


def getURLList(startURL):
	context = ssl._create_unverified_context()
	website = urllib.urlopen(startURL, context=context)
	print startURL
	#website = urllib2.urlopen(startURL)
	#read html code
	html = website.read()
	#use re.findall to get all the links
	links = re.findall('"((http|ftp)s?://.*?)"', html)
	return links

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
links = getURLList(starturl)

startRange = yearmap[year]
endRange = startRange + 100

for i in range(0, endRange):
	songname = songlist[i][1]
	for songpage in links:
		print songpage
		print songname