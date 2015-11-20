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
	#website = urllib2.urlopen(startURL)
	#read html code
	html = website.read()
	#print html
	#use re.findall to get all the links
	links = re.findall('<td>"<a href="/wiki/.*" title', html)
	#links = re.findall('"((http|ftp)s?://.*?)"', html)
	return links

def getTableURLS(beginpage):
	wikipage = wikipedia.page(beginpage)
	starturl = wikipage.url
	links = getURLList(starturl)
	actuallinks = []
	linkprefix = "https://www.wikipedia.org"
	for link in links:
		actuallink = linkprefix + link[14:-7]
		actuallinks.append(actuallink)
	return actuallinks

def getSongLengths(links):
	context = ssl._create_unverified_context()
	songdictionary = {}
	for link in links:
		website = urllib.urlopen(link, context=context)
		html = website.read()
		a = re.findall(lenghtexpr, html)
		if(len(a) > 0):
			songlength = re.findall(timeexpr, a[0])
			songdictionary[link] = songlength[0]
			print songdictionary[link]
	print len(songdictionary)
	return songdictionary
with open('data.csv', 'rb') as f:
	reader = csv.reader(f)
	songlist = list(reader)

lenghtexpr = re.compile('<th scope="row">Length</th>\n<td>[<b>]*\d*:\d\d')
timeexpr = re.compile('\d*:\d\d')
year = "1980"
beginpage = "Billboard Year-End Hot 100 singles of " + str(year)
yearmap = {}
j = 0;
for i in range(1980, 2010):
	yearmap[str(i)] = j
	j = j + 100

startRange = yearmap[year]
endRange = startRange + 100
links = getTableURLS(beginpage)
songdictionary = getSongLengths(links)


for i in range(startRange, endRange):
	songname = songlist[i][1]
	for songpage in links:
		x  = 1
		#print songpage
		#print songname