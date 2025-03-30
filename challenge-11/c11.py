import csv

data =[]

with open("data.csv") as f:
    reader = csv.reader(f)
    
    for row in reader:
        data.append(row)
print(data)
