import csv
import datetime as dt
import matplotlib.pyplot as plt


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



import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# True data
x = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
true_y = np.array([2.5, 4, 6.5, 8.75, 10])

# Fit linear regression model
model = LinearRegression()
model.fit(x, true_y)

# Predicted y-values from the linear regression model
predicted_y = model.predict(x)

# Calculate the residuals (difference between true y-values and predicted y-values)
residuals = true_y - predicted_y

# Plot the true data
plt.scatter(x, true_y, color='blue', label='True Data')

# Plot the linear regression line
plt.plot(x, predicted_y, color='red', label='Linear Regression Line')

# Plot the residuals (errors)
for i in range(len(x)):
    # plt.plot([x[i], x[i]], [true_y[i], predicted_y[i]], color='gray', linestyle='--')
    plt.plot([x[i], x[i]], [predicted_y[i], predicted_y[i] + residuals[i]], color='green', linestyle='-')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('True Data vs Linear Regression Line with Residuals')

# Add legend
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
