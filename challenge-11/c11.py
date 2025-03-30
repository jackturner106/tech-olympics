import csv
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = "data.csv"

data =[]
unique_whales = set()
sum = 0

with open(filename) as f:
    reader = csv.reader(f)
    
    for row in reader:
        data.append(row)

CUSTOMER_ID_IND = data[0].index("CustomerID")
TRANSACTION_AMOUNT_IND = data[0].index("TransactionAmount")
od = data[1:]
# step 1: filter:
data = [d for d in data[1:] if len(d) == 4]
data = [d for d in data if float(d[TRANSACTION_AMOUNT_IND]) > 100]

for d in data:
    unique_whales.add(d[CUSTOMER_ID_IND])

print("Unique Customers: {}".format(len(unique_whales)))

sum = 0
for d in od:
    if d[CUSTOMER_ID_IND] in unique_whales:
        sum += float(d[TRANSACTION_AMOUNT_IND])
print("Total Money Spent: {}".format(sum))
