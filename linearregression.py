import csv
import datetime
import time
import matplotlib.pyplot as plt
from sklearn import linear_model # pip install -U scikit-learn
from sklearn import metrics


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

def readdata2014():
	x = []
	y = []
	with open('out.csv', 'r') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if int(row[3]) == 2014:
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

def scatterplot(x, y):
        title = []
        time = []
        for i in range(len(x)):
                title.append(x[i][0])
                time.append(x[i][1])
        plt.scatter(title, y)
        plt.show()
        plt.scatter(time, y)
        plt.show()

def rsquared(regressiontype, ypredict, y1):
	print regressiontype
	print ypredict  # what do these values represent?
	metrics.r2_score(y1, ypredict)
	

def leastsquares(x,y, x1, y1):
	clf = linear_model.LinearRegression()
	clf.fit(x,y)
	ypredict = clf.predict(x1)
	rsquared("least squares",ypredict, y1)

def ridgeregression(x,y,x1,y1):
	clf = linear_model.RidgeCV(alphas=[.1,.5,1,10])
	clf.fit(x,y)
	ypredict = clf.predict(x1)
	rsquared("ridgeregression",ypredict, y1)

def lasso(x,y,x1,y1):
	clf = linear_model.LassoCV(alphas=[.1,.5,1,10])
	clf.fit(x,y)
	ypredict = clf.predict(x1)
	rsquared("lasso",ypredict, y1)

def logistic(x,y,x1,y1):
        clf = linear_model.LogisticRegression()
        clf.fit(x,y)
        ypredict = clf.predict(x1)
        rsquared("logistic", ypredict, y1)

def main():
	(x,y) = readdata()
	(x1, y1) = readdata2014()
	scatterplot(x,y)
	#scatterplot(x1,y1)
	leastsquares(x,y,x1,y1)
	ridgeregression(x,y,x1,y1)
	lasso(x,y,x1,y1)
	logistic(x,y,x1,y1)


if __name__ == "__main__": 
	main()
