'''
f=open("source.txt","r")
print(f.read(2))
f.close()
'''
'''
f=open("source.txt")
print(f.readline(),end="")
print(f.readline())
f.close()
'''
'''
f=open("source.txt","w")
f.write("hello how are you")
f.close()
'''
'''
f=open("source.txt","a")
f.write("\nhello how are you")
f.close()
'''
'''
f=open("abc.txt","w")
f.write("\nhello how are you")
f.close()
'''

#Examples

def readFile():
    f = open("source.txt")
    str1 = f.read()
    f.close()
    return str1

#1 count vowels
'''
var = readFile()

count = 0
for i in var:
    if i in "AEIOUaeiou":
        count=count+1
print("total vowels:",count)
'''
#2 count consonants
'''
var = readFile()
count = 0
for i in var:
    if i not in "AEIOUaeiou" and isalpha():
        count=count+1
print("total vowels:",count)
'''

#3 count lower and upper case letters
'''
var = readFile()

lower = 0
upper =0
for i in var:
    if i.islower():
        lower=lower+1
    elif i.isupper():
        upper=upper+1
print("lower letters:",lower)
print("upper letters:",upper)
'''

#4 count words
'''
var = readFile()
list1=var.split()
print("no of words:",len(list1))
'''
#5- count punctuations
'''
import string
var = readFile()
count = 0
for i in var:
    if i in string.punctuation:
        count=count+1
print("total punctuation:",count)
  '''
#6 count lines
'''
var = readFile()
list1=var.split("\n")
print("no of lines:",len(list1))
'''

#7 convert all the char to upper case
'''
var= readFile()
f = open("source.txt","w")
f.write(var.upper())
f.close()
'''


