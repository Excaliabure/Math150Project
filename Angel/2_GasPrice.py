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

my_list = [ 5, 6,7]
for i in range(7, 0, -1):  # Loop in reverse to append to the beginning
    my_list.insert(0, i)
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]


# Initialize an empty dictionary
my_dict = {}

# Define the range for the loop
start = 1
end = 10

# Assuming you have a dictionary named 'my_dict'
my_dict = {'key_1': 1, 'key_2': 2, 'key_3': 3}

# Specify the value you are searching for
value_to_find = 2

# Iterate over the dictionary keys and check for the value
for key in my_dict:
    if my_dict[key] == value_to_find:
        print("The key corresponding to the value", value_to_find, "is:", key)
        break  # Exit the loop once the key is found

# If the value is not found in the dictionary
else:
    print("Value", value_to_find, "not found in the dictionary.")


