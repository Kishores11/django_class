#Dictionary examples
'''
squares = {}
for i in range(1,11):
    squares[i]=i*i
print(squares)
'''

'''
even = {}
odd = {}
for i in range(1,11):
    if i%2==0:
        even[i]=i*i
    else:
        odd[i]=i**3

print(even)
print(odd)
'''

data = {}

def newStudent():
    print("-------Add new student----")
    name=input("enter students name:")  #key
    #value
    s1=int(input("enter marks in sub1:"))
    s2=int(input("enter marks in sub2:"))
    s3=int(input("enter marks in sub3:"))

    data[name]=[s1,s2,s3]
    print("-----student added successfully-----")

def checkPerc():
        print("------check your percentage here------")
        n=input("enter your name to check:")
        if n in data:
            print("------data found-----")
            print(data[n])
            perc=sum(data[n])/3
            print("percentage:%,2f"%perc)
            print("-"*30)
        else:
            print("-----data not found-----")

while True:
    print("1. Add\n2. Check\n3. Exit")
    ch = int(input("enter:"))

    if ch==1:
        newStudent()

    elif ch==2:
        checkPerc()

    elif ch==3:
        print("------bye-----")
        break
    else:
        print("----invalid choice---")
