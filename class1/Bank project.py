#Bank Application Project
#dictionary data type

# {101:{name:sam,age:25,amount:10000}}

bank = {}  # Empty dictionary

def newAccount():
    print("----- Create A New Account Here -----")

    acc = input("Enter new account number:") # key
    # value
    list1 = ["Name","Age","Address","Phone","Amount"]
    list2 = []
    n = input("Enter name:")
    while n.isalpha() != True:
        print("Invalid name ! Please try again")
        n = input("Enter name:")
    list2.append(n)
    
    age = input("Enter age:")
    while age.isdigit() != True:
        print("Invalid age ! Please try again")
        age = input("Enter age:")
    list2.append(age)
    
    add = input("Enter address:")
    list2.append(add)
    ph = input("Enter phone number:")
    list2.append(ph)
    amt = int(input("Enter amount:"))
    list2.append(amt)

    # Store data into dictionary
    bank[acc] = dict(zip(list1,list2))
    print("----- Account Created Successfully -----\n")

def existingCust():
    print("---- For Existing Customer ----")
    acc = input("Enter your account number to fetch your details:")
    if acc in bank:
        print("---- Data Found ----")
        while True:
            print("1. Check Balance\n2. Withdraw\n3. Deposite\n4. Main Menu")
            ch = int(input("Enter your choice:"))
            if ch == 1:
                print("-"*30)
                print("Available Balance:",bank[acc]["Amount"])
                print("-"*30)
            elif ch == 2:
                amt_w=int(input("Enter amount to withdraw:"))
                if amt_w<bank[acc]['Amount']:
                    bank[acc]['Amount'] = bank[acc]['Amount']-amt_w
                    print("-"*30)
                    print("Remaining Balance :",bank[acc]['Amount'])
                    print("-"*30)
                else:
                    print("--- Insufficient Balance ---")
            elif ch == 3:
                amt_w=int(input("Enter amount to deposite:"))
                bank[acc]['Amount'] = bank[acc]['Amount']+amt_w
                print("-"*30)
                print("Deposite Successfull ! Available Balance :",bank[acc]['Amount'])
                print("-"*30)
            elif ch == 4:
                break               
    else:
        print("---- Data Not Found ----")

def updateDetails():
    print("------update details-------")
    acc=input("enter your acc no to fetch:")
    if acc in bank:
        print("---- Data Found ----")
        while True:
            print("1. update phone\n2. update address")
            ch = int(input("Enter your choice:"))
            if ch==1:
                print("-"*30)
                old_ph=int(input("enter old phone no:"))
                if old_ph==bank[acc]['phone']:
                    bank[acc]['phone']=int(input("enter new phone:"))


    
    

while True:
    print("****** MAIN MENU ******")
    print("1. Create A New Account")
    print("2. For Existing Customer")
    print("3. Update Details")
    print("4. Exit")
    ch = int(input("Enter your choice:"))
    if ch == 1:
        newAccount()  # function call
    elif ch == 2:
        existingCust()  # function call
    elif ch == 3:
        updateDetails()   # function call        
    elif ch == 4:
        print("--- Thank You ! Please visit again ---")
        break
    else:
        print("--- Invalid Choice ---")
