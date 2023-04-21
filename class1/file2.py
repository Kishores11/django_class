#csv file handling
#comma seperated values

import csv

# reading data from csv file

f=open("source.csv","r")
data = list(csv.reader(f))
print(data)

f.close()


#writing data csv file
#w mode or a mode
'''
f = open("source.csv","w",newline="")

obj = csv.writer(f)
obj.writerrow(["sam",sam@email.com])
obj.writerrow(["john",john@email.com])
obj.writerrow(["mike",mike@email.com])
'''
