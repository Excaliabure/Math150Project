import csv
import datetime as dt
import matplotlib.pyplot as pl


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




dates = [dt.datetime.strptime(date, '%b %d, %Y') for date in xdate]
ximport = [float(i) for i in ximport]
pl.plot(dates,ximport)
pl.title('barel vs tim')
pl.show()
