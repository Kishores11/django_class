# Regular expressions

import re

#search() and findall()

#1
'''
match = re.search("hello","hello how are you")
print(match.group()) #will print the matching pattern
'''

#2
'''
pat = "car"
txt =open("data1.txt").read()

match = re.search(pat,txt)
if match:
    print("Match Found:",match.group())
else:
    print("Match not found")
'''

# findall()
# will return a list of all matching pattern
'''
pat = "hello"
txt =open("data1.txt").read()

match = re.findall(pat,txt)
print(match)
'''
# data2
# \d - True for digits 0-9
# + - 1 or more
# pat = "\d\d"
'''
pat = "\d\d"
txt =open("data2.txt").read()
match = re.findall(pat,txt)
print(match)
'''
'''
pat = "\d+"
txt =open("data2.txt").read()
match = re.findall(pat,txt)
print(match)
'''

# data 3
# \s - True for space

##pat = "\d\d\d-\d\d\d-\d\d\d\d"

pat = "\d{3}[-\s*]\d{3}[-\s*]\d{4}"
txt =open("data3.txt").read()
match = re.findall(pat,txt)
print(match)















