data={}
def signIn():
    n=input("enter name:")
    p=input("enter password:")
    data[n]=p
    print("sign up successful")
    print(data)

def logIn():
    n=input("enter your name to login:")
    if n in data:
        print("---Account found---")
        p=input("enter Password:")
        if p==data[n]:
            print("---login successful!!---")
        else:print("---Invalid Password!! Login Again with correct password---")
    else:print("Invalid Account!!")
    
while True:
    print("\n1. sign in\n2. login")
    ch=int(input("enter:"))

    if ch==1:
        signIn()

    elif ch==2:
        logIn()

    else:
        print("-----invalid----")
           
