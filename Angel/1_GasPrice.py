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

with open('/Users/angelgonzalezguevara/Documents/Crude Oil'
          '/Data 1-Table 1.csv','r') as file:
    reader = csv.reader(file)
    next(reader)
    next(reader)
    next(reader)
    next(reader)
    xdates = []
    xBarPr = []
    for row in reader:
        xdates.append(row[0])
        xBarPr.append(row[1])

dates = [dt.datetime.strptime(date, '%b %d, %Y') for date in x]
datesforCr = [dt.datetime.strptime(date, '%b %d, %Y').timestamp() for date in xdates]

datesforR2 = [dt.datetime.strptime(date, '%b %d, %Y').timestamp() for date in x]
x2int = [float(i) for i in x2]  # gas prices
x2Cr = [float(i) for i in xBarPr] # crude oil barrel prices

dates = np.array(dates).reshape(-1,1)
x2int = np.array(x2int).reshape(-1,1)
x2Cr = np.array(x2Cr).reshape(-1,1)
datesforR2 = np.array(datesforR2).reshape(-1,1)

datesforCr = np.array(datesforCr).reshape(-1,1)

ypred = sk.LinearRegression().fit(datesforR2,x2int).predict(datesforR2)
rsqu = sk.LinearRegression().fit(datesforR2,x2int).score(datesforR2,x2int)

ypredCR = sk.LinearRegression().fit(datesforCr,x2Cr).predict(datesforCr)
rsquCR = sk.LinearRegression().fit(datesforCr,x2Cr).score(datesforCr,x2Cr)

xgasp =[]
xcrudep = []
dateforGasprice =[]
dateforCrPrice=[]
for i in range(len(dates)):
    if dates[i] == datesforCr[i]:
        continue
    xgasp.append(x2int[i])
    xcrudep.append(x2Cr[i])
    dateforGasprice.append(dates[i])


plt.subplot(1,4,1)
plt.scatter(dates, x2int,s=[5])
plt.plot(dates,ypred,color='red')
plt.title('Price of Gas (1994'+ '-Present), R^='+str(np.round(rsqu,2)))
plt.subplot(1,4,2)
plt.plot(datesforCr, x2Cr)
plt.plot(datesforCr,ypredCR,color='red')
plt.title('Price of Crud Oil (1994'+ '-Present), R^='+str(np.round(rsquCR,2)))
plt.xlabel('Date')

# cluster
X = []
xgaspr = x2int.tolist()
xcrudepr = x2Cr.tolist()

xgaspr = [item for sublist in xgaspr for item in sublist]
xcrudepr = [item for sublist in xcrudepr for item in sublist]
for i,j in zip(xcrudepr,xgaspr):
    X.append([i,j])



crudeoilprices = [price[0] for price in X] # 
gasprices = [price[1]*10 for price in X]


# 50 EMA
ema250 = []
ema50 =[]
ema10=[]
pre_ema = xcrudepr[0]
pre_ema1 = xcrudepr[0]
pre_ema2 = xcrudepr[0]
EMA250 = lambda a, x: a * x + (1-a)* pre_ema

EMA50 = lambda a, x: a * x + (1-a)* pre_ema1

EMA10 = lambda a, x: a * x + (1-a)* pre_ema2

for i in list(range(len(xcrudepr))):
    if i % 250 == 0:
        pre_ema=xcrudepr[i]
    if i % 50 == 0:
        pre_ema1=xcrudepr[i]
    if i % 10 == 0:
        pre_ema2 = xcrudepr[i]
    s = 2/(len(list(range(len(xcrudepr)))) + 1)
    
    ema_ = EMA250(s,xcrudepr[i])
    ema1_ = EMA50(s,xcrudepr[i])
    ema2_ = EMA10(s,xcrudepr[i])
    pre_ema = ema_
    pre_ema1 = ema1_
    pre_ema2 = ema2_
    ema250.append(ema_)
    ema50.append(ema1_)
    ema10.append(ema2_)
    



# Show plot
plt.subplot(1,4,3)
plt.scatter(dateforGasprice,gasprices,s=[5])
plt.scatter(dateforGasprice,crudeoilprices,s=[5])
plt.figure()
plt.plot(datesforCr, x2Cr, linewidth = 2,  color = 'black',label='Price',linestyle = '--')
plt.plot(datesforCr,ema250, linewidth = 1, color = 'red',label='250 ema')
plt.plot(datesforCr,ema50,linewidth = 1, color='blue',label = '50 ema')
plt.plot(datesforCr,ema10,linewidth = 1, color='m',label = '10 ema')
plt.legend()
plt.show()


with open('/Users/angelgonzalezguevara/Documents/import(supply)ofCrudeOil'
          '/Data 1-Table 1.csv','r') as file:
    reader = csv.reader(file)
    next(reader)
    next(reader)
    next(reader)
    xdate = []
    ximport = []
    for row in reader:
        xdate.append(row[0])
        ximport.append(row[1])
    xdate.pop()
    ximport.pop()



dates = [dt.datetime.strptime(date, '%b %d, %Y') for date in xdate]


