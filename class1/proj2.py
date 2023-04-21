
data=[]

while True:
    print("1. Add Data\n2. Search Data\n3. Delete Data\n4. Exit")
    ch = int(input("enter choice:"))

    if ch==1:
        n=input("enter name:")
        p=input("enter ph no:")
        a=input("enter address:")
        data.append([n,p,a])
        print("-----data added-----")
        print(data)
        

    elif ch==2:
        n=input("enter your name to search:")
        for i in data:
            count=0
            if n in i:
                count=count+1
                print(i)
                print("-"*30)
        if count==0:
            print("------Data not found-----")

    elif ch==3:
        n=input("enter you name to del:")
        for i in data:
            count=0
            if n in i:
                count=count+1
                data.remove(i)
                print("data deleted")
                print('-'*30)
        if count==0:
            print("---data not found-----")

    elif ch==4:
        print("-----bye----")
        break
    else:
        print("-----invalid choice----")
            
