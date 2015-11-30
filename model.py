import csv

def gettitlelength(title):
	if '(' in title:
		title = title.split("(")
		title = title[0]
	return len(title)


def readdata():
	x = []
	y = []
	with open('out.csv', 'r') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if int(row[3]) < 2014:
				rank = row[0]
				title = row[1]
				length = row[4]
				titlelength = gettitlelength(title)
				y.append(rank)
				x.append([titlelength, length])
		return (x,y)



def main():
	(x,y) = readdata()
	print len(y)
	print len(x)

if __name__ == "__main__": 
	main()