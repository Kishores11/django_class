
data=[]

while True:
    print("1. Add Data\n2. Search Data\n3. Delete data\n4. exit")
    ch=int(input('enter choice:'))

    if ch==1:
        n = input("Enter name:")
        p = input("Ente phone number:")
        a = input("Enter address:")

        data.append([n,p,a])
        print("-------data added successfully-------")
        print(data)

    elif ch==2:
        n=input("enter name to search your details:")
        count = 0
        for i in data:
            if n in i:
                count = count+1
                print(i)
                print('-'*30)
        if count == 0:
            print("--- Data Not Found ---")

    elif ch==3:
        n=input("enter name to delete your details:")
        count = 0
        for i in data:
            if n in i:
                count = count+1
                data.remove(i)
                print("Data Deleted!!!")
                print('-'*30)
        if count == 0:
            print("--- Data Not Found ---")
            
    elif ch==4:
        print("bye")
        break
    else:
        print('-----INVALID CHOICE!----')
