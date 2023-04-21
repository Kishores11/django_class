name=[]
phone=[]
address=[]

while True:
    print("1. Add Data\n2. Search Data\n3. Delete Data\n4. Exit")
    ch = int(input("enter choice:"))

    if ch==1:
        n=input("enter name:")
        name.append(n)
        p=input("enter ph no:")
        phone.append(p)
        a=input("enter address:")
        address.append(a)

        print("---------Data Added Sucessfully------")

    elif ch==2:
        n=input("enter your name to search:")
        if n in name:
            print("------Data Found----")
            index_num=name.index(n)
            print("Name:",name[index_num])
            print("ph no:",phone[index_num])
            print("Address:",address[index_num])
            print("-"*30)
        else:
            print("------Data not found-----")

    elif ch==3:
        n=input("enter you name to del:")
        if n in name:
            print("----Data found----")
            index_num=name.index(n)
            name.pop(index_num)
            phone.pop(index_num)
            address.pop(index_num)
            print("-----data deleted-----")

        else:
            print("---data not found-----")

    elif ch==4:
        print("-----bye----")
        break
    else:
        print("-----invalid choice----")
            
