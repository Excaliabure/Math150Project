import matplotlib.pyplot as plt
import numpy as np
import csv
import datetime as dt
import math as m
import sklearn.linear_model as sk
import sklearn.cluster as skc


with open('/Users/angelgonzalezguevara/Downloads/pswrgvwall.csv','r') as file:
    reader = csv.reader(file)
    next(reader)
    next(reader)
    next(reader)
    
    x=[]
    x2=[]
    xdat =[]
    xdat2=[]
    for row in reader:
        x.append(row[0])
        x2.append(row[1])
    x.pop()
    x2.pop()

with open('/Users/angelgonzalezguevara/Documents/Crude Oil/Data 1-Table 1.csv','r') as file:
    reader = csv.reader(file)
    print(next(reader))
    print(next(reader))
    print(next(reader))
    xdates = []
    xBarPr = []
    for row in reader:
        xdates.append(row[0])
        xBarPr.append(row[1])

dates = [dt.datetime.strptime(date, '%b %d, %Y') for date in x]
datesforCr = [dt.datetime.strptime(date, '%b %d, %Y') for date in xdates]

datesforR2 = [dt.datetime.strptime(date, '%b %d, %Y').timestamp() for date in x]
x2int = [float(i) for i in x2]  # gas prices
x2Cr = [float(i) for i in xBarPr] # crude oil barrel prices

dates = np.array(dates).reshape(-1,1)
x2int = np.array(x2int).reshape(-1,1)
x2Cr = np.array(x2Cr).reshape(-1,1)
datesforR2 = np.array(datesforR2).reshape(-1,1)

ypred = sk.LinearRegression().fit(datesforR2,x2int).predict(datesforR2)
rsqu = sk.LinearRegression().fit(datesforR2,x2int).score(datesforR2,x2int)

xgasp =[]
xcrudep = []
for i in range(len(dates)):
    if dates[i] == datesforCr[i]:
        continue
    xgasp.append(x2int[i])
    xcrudep.append(x2Cr[i])


plt.subplot(1,4,1)
plt.scatter(dates, x2int,s=[5])
plt.plot(dates,ypred,color='red')
plt.title('Price of Gas (1994'+ '-Present), R^='+str(np.round(rsqu,2)))
plt.subplot(1,4,2)
plt.scatter(datesforCr, x2Cr,s=[5])
plt.xlabel('Date')
plt.subplot(1,4,3)
plt.scatter(xcrudep, xgasp,s=[5])
plt.grid(True)

# cluster
X = []
xgaspr = x2int.tolist()
xcrudepr = x2Cr.tolist()

xgaspr = [item for sublist in xgaspr for item in sublist]
xcrudepr = [item for sublist in xcrudepr for item in sublist]
for i,j in zip(xcrudepr,xgaspr):
    X.append([i,j])


kmeans = skc.KMeans(n_clusters=5).fit(X)
ykmean = skc.KMeans(n_clusters=5).fit(X).predict(X)
crudeoilprices = [price[0] for price in X]
gasprices = [price[1] for price in X]

# Show plot
plt.subplot(1,4,4)
plt.scatter(crudeoilprices,gasprices, c = ykmean)
plt.show()
