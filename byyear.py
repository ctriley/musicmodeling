#byyear2.py

import urllib2
import re
import unicodecsv as csv
import wikipedia
import ssl
import urllib
import sys


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

def getSongInfo(beginpage):
	context = ssl._create_unverified_context()
	wikipage = wikipedia.page(beginpage)
	starturl = wikipage.url
	website = urllib.urlopen(starturl, context=context)
	#website = urllib.urlopen(starturl, context=context)
	html = website.read()
	table_entries = re.findall('<tr>\n<th scope="row">\d+</th>\n<td>"<a href="/wiki/.*" title.*\n<td><a href=".*" title', html)
	ranklist = {}
	for entry in table_entries:
		rank = re.findall('<th scope="row">\d+</th>', entry)
		rank = rank[0][16:-5]
		linkprefix = "https://www.wikipedia.org"
		link = re.findall('<td>"<a href="/wiki/.*" title', entry)
		actuallink = linkprefix + link[0][14:-7]
		artistname = entry.split("\n")
		artistname = artistname[3]
		artistname = artistname[19:-7]
		row = [actuallink, artistname]
		ranklist[rank] = row
	return ranklist


def getSongLengths(links, year):
	context = ssl._create_unverified_context()
	lenghtexpr = re.compile('<th scope="row">Length</th>\n<td>[<b>]*\d*:\d\d')
	timeexpr = re.compile('\d*:\d\d')
	songnamexpr = re.compile('<title>.* - Wikipedia, the free encyclopedia</title>')
	songdictionary = {}
	for key in links:
		row = links[key]
		link = row[0]
		print link
		try:
			website = urllib2.urlopen(link, context=context)	# fails here
			html = website.read().decode("utf-8")
			lengthregx = re.findall(lenghtexpr, html)
			titles = re.findall('<title>.* - Wikipedia, the free encyclopedia</title>', html)
			title = titles[0][7:-43]
			if(len(lengthregx) > 0):
				songlength = re.findall(timeexpr, lengthregx[0])
				entry = [title, row[1], year, songlength[0]]
				songdictionary[key] = entry
		except:
			"encountered exception"
	return songdictionary


def writeyear(year):
	beginpage = "Billboard Year-End Hot 100 singles of " + str(year)
	ranklist = getSongInfo(beginpage)
	songdictionary = getSongLengths(ranklist, year)
	#print songdictionary
	with open('out5.csv', 'a') as out: # 'a' opens the file for appending 'w' for overwriting
		writer = csv.writer(out)
		for key in songdictionary:
			dictionaryrow = songdictionary[key]
			csvrow = [key, dictionaryrow[0], dictionaryrow[1], dictionaryrow[2], dictionaryrow[3]]
			writer.writerow(csvrow)

def main():
	for year in range(1982,2015):
		print str(year)
		writeyear(year)

if __name__ == "__main__": 
	main()


#with open('data.csv', 'rb') as f:
#	reader = csv.reader(f)
#	songlist = list(reader)
#yearmap = {}
	#j = 0;

	#for i in range(1980, 2010):
	#	yearmap[str(i)] = j
	#	j = j + 100

	#startRange = yearmap[year]
	#endRange = startRange + 100
	#links = getTableURLS(beginpage)
