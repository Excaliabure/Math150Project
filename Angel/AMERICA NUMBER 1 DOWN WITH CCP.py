import matplotlib.pyplot as plt
import numpy as np
import csv
import datetime as dt
import math as m
import sklearn.linear_model as sk
import sklearn.tree as skt
# nice car

with open('/Users/angelgonzalezguevara/Downloads/pswrgvwall.csv','r') as file:
    reader = csv.reader(file)
    next(reader)
    next(reader)
    print(next(reader))
    
    x=[]
    x2=[]
    xdat =[]
    xdat2=[]
    for row in reader:
        x.append(row[0])
        x2.append(row[1])
    x.pop()
    x2.pop()

dates = [1994 + date/len(x) * (2023-1994) for date in range(len(x))]
x2int = [float(i) for i in x2]

dates = np.array(dates).reshape(-1,1)
x2int = np.array(x2int)


ypred = sk.LinearRegression().fit(dates,x2int).predict(dates)
rsqu = sk.LinearRegression().fit(dates,x2int).score(dates,x2int)

plt.scatter(dates, x2int,s=[5])
plt.plot(dates,ypred,color='red')
plt.title('Pruce of Gas (1994'+ '-Present), R^='+str(np.round(rsqu,2)))
plt.xlabel('Date')

# plt.grid(True)

# Format date on x-axis

# Rotate and align the x labels


# Show plot
plt.show()
