import re,csv
import os

path = "C:\\Users\\Kishore.saravanan\\Documents\\Python_Class\\Final_project"
var = os.listdir(path)

list_files = []
daily_profit = []


for i in var:
    if i.endswith(".txt"):
        list_files.append(i)

for item in list_files:
    txt = open(item).read()

    pat1 = "Product:\s(\w+)"
    prod = re.findall(pat1,txt)


    pat2 = "Quantity:\s(\w+)"
    quan = re.findall(pat2,txt)


    pat3 = "CP:\s(\w+)"
    cp = re.findall(pat3,txt)


    pat4 = "SP:\s(\w+)"
    sp = re.findall(pat4,txt)


    # Generate report in CSV
    filename = item.rstrip(".txt") + ".csv"
    
    f = open(filename,"w",newline="")
    obj = csv.writer(f)
    obj.writerow(["Product","Quantity","CP","SP","Profit"])
    total = 0
    for i in range(len(prod)):
        profit = (int(sp[i])-int(cp[i])) * int(quan[i])
        total = total+profit
        obj.writerow([prod[i],quan[i],cp[i],sp[i],profit])

    obj.writerow(["","","","Total",total])
    daily_profit.append(total)
    f.close()

print(list_files)
print(daily_profit)


# plot the graph
import matplotlib.pyplot as plt

plt.bar(list_files,daily_profit)
plt.title("December Report")
plt.xlabel("Dates")
plt.ylabel("Profit")
plt.show()
