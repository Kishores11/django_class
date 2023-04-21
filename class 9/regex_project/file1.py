# Supermarket DB Mgmt

#1 extract data
#2 generate report in csv
#profit = (sp-cp)*quantity
#3 plot graph

import re,csv

txt = open("source.txt").read()

pat1 = "Product:\s(\w+)"
prod = re.findall(pat1,txt)
print(prod)

pat2 = "Quantity:\s(\w+)"
quan = re.findall(pat2,txt)
print(quan)

pat3 = "CP:\s(\w+)"
cp = re.findall(pat3,txt)
print(cp)

pat4 = "SP:\s(\w+)"
sp = re.findall(pat4,txt)
print(sp)

# generate csv report

f = open("report.csv","w",newline="")
obj = csv.writer(f)
obj.writerow(["Product","Quantity","CP","SP","Profit"])
total = 0
for i in range(len(prod)):
     profit = (int(sp[i])-int(cp[i]))* int(quan[i])
     total = total + profit
     obj.writerow([prod[i],quan[i],cp[i],sp[i],profit])

obj.writerow(["","","","Total",total])
f.close()
    
    


