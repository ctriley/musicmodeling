## get song length from wikipedia.
import re
import csv
import wikipedia

# import csv file (Data)

with open('data.csv', 'rb') as f:
	reader = csv.reader(f)
	songlist = list(reader)
# regular expression needs generalizing for other songs
# need to output result into csv
expr = re.compile('class="min">(\d)*</span>:<span class="s">(\d)+')
for line in songlist:
	#pagetitle = wikipedia.suggest(line[1] + " music")
	#if(pagetitle != None):
	try:
		test = wikipedia.page("hotline bling") # replace "hotline bling" with line[1]
		s = test.html()
		search = expr.search(s)
		print search
		if(search != None):
			span = search.span()
			(x,y) = span
			sub = s[x:y]
			length = len(sub)
			
	except wikipedia.exceptions.PageError:
		print "page not found"
			# do nothing
	except wikipedia.exceptions.DisambiguationError:
		print "too many results"