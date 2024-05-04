import matplotlib.pyplot as plt
import numpy as np
import csv
import datetime as dt
import math as m
import sklearn.linear_model as sk
import sklearn.cluster as skc
import random

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
    if dates[i] != datesforCr[i]:
        xgasp.append(x2int[i])
        xcrudep.append(x2Cr[i])
        dateforGasprice.append(dates[i])

    

# plt.subplot(1,4,1)
# plt.scatter(dates, x2int,s=[5])
# plt.plot(dates,ypred,color='red')
# plt.title('Price of Gas (1994'+ '-Present), R^='+str(np.round(rsqu,2)))
# plt.subplot(1,4,2)
# plt.plot(datesforCr, x2Cr)
# plt.plot(datesforCr,ypredCR,color='red')
# plt.title('Crud Oil (1994'+ '-Present), R^='+str(np.round(rsquCR,2)))
# plt.xlabel('Date')


X = []
xgaspr = x2int.tolist()
xcrudepr = x2Cr.tolist()

xgaspr = [item for sublist in xgaspr for item in sublist]
xcrudepr = [item for sublist in xcrudepr for item in sublist]
for i,j in zip(xcrudepr,xgaspr):
    X.append([i,j])




crudeoilprices = [price[0] for price in X] # 
gasprices = [price[1]* 7 for price in X]


# 50 and 200 EMA
ema200 = []
ema50 =[]
pre_ema = xcrudepr[0]
pre_ema1 = xcrudepr[0]

EMA50 = lambda a, x: (a * x) +(1-a)*(pre_ema)

EMA200 = lambda a, x: (a * x) + (1-a)*(pre_ema1)


for i in list(range(len(xcrudepr))):
    if i % 50 == 0:
        pre_ema=xcrudepr[i]
    if i % 200 == 0:
        pre_ema1=xcrudepr[i]
    
    s1 = 2/(50 + 1)
    s2 = 2/(200 + 1)
    
    ema_ = EMA50(s1,xcrudepr[i])
    ema1_ = EMA200(s2,xcrudepr[i])
    
    pre_ema = ema_
    pre_ema1 = ema1_
    
    ema50.append(ema_)
    ema200.append(ema1_)
    
    

datesforCr = [dt.datetime.strptime(date, '%b %d, %Y') for date in xdates]


# Show plot
plt.figure()
plt.plot(dateforGasprice,gasprices, label = "Gas Price (scaled up 10x)")
plt.plot(dateforGasprice,crudeoilprices,label = "Crude Oil Price")
plt.legend()
plt.figure()
plt.title("Crude Oil Prices(1994-Present)")
plt.xlabel("Time")
plt.ylabel("Price (in USD)")
plt.plot(datesforCr, x2Cr, linewidth = 2,  color = 'black',label='Price',linestyle = '--')
plt.plot(datesforCr,ema50, linewidth = 1, color = 'magenta',label='50 ema')
plt.plot(datesforCr,ema200,linewidth = 1, color='blue',label = '200 ema')

plt.legend()
plt.show()

# import of crude oil 
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

ximport = [float(i) for i in ximport] 

###########################
maxofp = []

dates_ = [dt.datetime.strptime(date, '%b %d, %Y').timestamp() for date in xdate]


for i in range(1,56):
    shift = []

    shift = x2Cr[:i].tolist()
    shift = [item for sublist in shift for item in sublist]
    crudeoilprices = shift + crudeoilprices
    crudeoilprices = crudeoilprices[:-i]

    gasprices = np.array(gasprices).reshape(-1,1)
    crudeoilprices = np.array(crudeoilprices).reshape(-1,1)
    corrcoeff = sk.LinearRegression().fit(gasprices,crudeoilprices).score(gasprices,crudeoilprices)

    gasprices = gasprices.tolist()
    crudeoilprices = crudeoilprices.tolist()

    gasprices = [item for sublist in gasprices for item in sublist]
    crudeoilprices = [item for sublist in crudeoilprices for item in sublist]

    gasprices = gasprices[i:]
    crudeoilprices = crudeoilprices[i:]

    maxofp.append(corrcoeff)

################################



## Finding days and shift for Corr. Coeff.
corr = max(maxofp)
# befro shuft
print(f"p = {maxofp[0]} for curde oil without a shift of {maxofp.index(maxofp[0])}")

print(f"p = {max(maxofp)} for curde oil with a shift of {maxofp.index(max(maxofp))} " )

####################


