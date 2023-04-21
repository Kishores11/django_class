class SmallError(Exception):
    pass
class LargeError(Exception):
    pass


    
import random
ch = int(input("enter no of players:"))
for i in ch:
    str1=input("enter player no %i:")
    str2=input("enter player no %i:")
    str3=input("enter player no %1:")
        
start = int(input("enter start value:"))
stop = int(input("enter stop value:"))
print("picking one random no between" start "and" stop)
number = random.randint(start,stop)

while True:
    print("-------GUESS THE NUMBER---------")
    print("Press '1' to start")
    print("Press '2' to exit")
    ch=int(input("Enter choice:"))

    if ch == 1:
        playGame()
    elif ch == 2:
        break
    


try:
    if num<number:
        raise SmallError
    elif num>number:
        raise LargeError
    else:
        break

except SmallError:
    print("Your number is SMALL ! Please guess the BIG number")
except LargeError:
    print("Your number is BIG ! Please guess the SMALL number")

print("Congratulations ! You won the game")


    
    
              


