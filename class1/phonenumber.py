ph=str(input("enter phone no:"))
len1=len(ph)
while True:
    if len1==12:
        if ph[0].isdigit() and ph[1].isdigit() and ph[2].isdigit()  and ph[3]=="-" and ph[4].isdigit() and ph[5].isdigit() and ph[6].isdigit  and ph[7]=="-" and ph[8].isdigit() and ph[9].isdigit() and ph[10].isdigit() and ph[11].isdigit():
            print("valid")
        else:
            print("invalid")
        
        
