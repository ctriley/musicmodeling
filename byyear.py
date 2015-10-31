import re
import csv
import wikipedia
import requests

with open('data.csv', 'rb') as f:
	reader = csv.reader(f)
	songlist = list(reader)
expr = re.compile('class="min">(\d)*</span>:<span class="s">(\d)+')

beginpage = "Billboard Year-End Hot 100 singles of 1980"

wikipage = wikipedia.page(beginpage)
for i in range(100):
	songname = songlist[i][1]
	for songpage in wikipage.links:
		print songpage
		print songname
		if(songpage == songname):
			url = songpage.geturl()			# need to figure out how to get the url for each page
			print url
			resp = requests.get(url, params={'action': 'raw'})
			page = resp.text
			for line in page.splitlines():
				if line.startswith('| Length'):
					length = line.partition('=')[-1].strip()
					break
			print length