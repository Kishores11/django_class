
# pip install matplotlib
# google colab

import csv
import matplotlib.pyplot as plt

def addData():
  print("--- Add New Data Here ---")
  # country name, positive case, recovered cases and death cases

  f = open("corona.csv","a",newline="")
  obj = csv.writer(f)
  cn = input("Enter country name:")
  pc = input("Enter total positive cases:")
  rc = input("Enter total recovered cases:")
  dc = input("Enter total death cases:")

  obj.writerow([cn,pc,rc,dc])
  f.close()
  print("--- Data Added Successfully ---")

def showData():
  print("-- Display Data Here --")

  f = open("corona.csv")
  data = list(csv.reader(f))
  for i in data:
    print(i)
  print("-"*30)
  f.close()

def plotData():
  f = open("corona.csv")
  data = list(csv.reader(f))

  country_name = []
  positive_cases = []
  recovered_cases = []
  for i in data:
    country_name.append(i[0])
    positive_cases.append(int(i[1]))
    recovered_cases.append(int(i[2]))
  # print(country_name)
  # print(positive_cases)

  plt.bar(country_name,positive_cases)
  plt.bar(country_name,recovered_cases)
  plt.xlabel("Country Name")
  plt.ylabel("Positive Cases/Recovered Cases")
  plt.title("Corona Graph")
  plt.show()

while True:
  print("1. Add Data\n2. Show Data\n3. Plot Data\n4. Exit")
  ch = int(input("Enter choice:"))

  if ch == 1:
    addData()
  elif ch == 2:
    showData()
  elif ch == 3:
    plotData()
  elif ch == 4:
    break
  else:
    print("--Invalid Choice --")
