import csv
import datetime
import time
from sklearn import linear_model # pip install -U scikit-learn


def gettitlelength(title):
	if '(' in title:
		title = title.split("(")
		title = title[0]
	return len(title)

def mintosec(songtime):
	while(len(songtime)) < 8:
		if len(songtime) == 2 or len(songtime) == 5:
			songtime = ':' + songtime
		else: 
			songtime = '0' + songtime # 00003:45
	try:
		x = time.strptime(songtime,'%H:%M:%S')
		totalseconds = datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,
			seconds=x.tm_sec).total_seconds()
		return totalseconds
	except:
		return None

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
				length = mintosec(length)
				if length != None:
					titlelength = gettitlelength(title)
					y.append(int(rank))
					titlelength = int(titlelength)
					length = int(length)
					x.append([titlelength, length])
		return (x,y)

def leastsquares(x,y):
	clf = linear_model.LinearRegression()
	clf.fit(x,y)
	print('Coefficients: \n', clf.coef_)

def main():
	(x,y) = readdata()
	leastsquares(x,y)

if __name__ == "__main__": 
	main()