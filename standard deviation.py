import math
import csv
with open("C:/Users/arkma/Dropbox/My PC (DESKTOP-F2428EU)/Desktop/data.csv",newline="") as f:
    reader = csv.reader(f)
    file_data = list(reader)
data = file_data[0]
def mean(data):
    n = len(data)
    total = 0
    for x in data:
        total = total + int(x)
    mean = total/n
    return mean
array = []
for i in data:
    a = int(i) - mean(data)
    a = a**2
    array.append(a)
sum = 0
for i in array :
    sum = sum + i

result = sum /(len(data)-1)
sd = math.sqrt(result)
print(sd)