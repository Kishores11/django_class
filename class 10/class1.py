# self parameter
'''
class Employee:
    def f1(self):
        print("Hello World")

    def f2(self):
        print("Hello Python")

emp1 = Employee()
emp1.f1()
Employee.f1(emp1)
emp1.f2()
'''

# instance inside method
'''
class Employee:
    def f1(self):
        self.name = "Sam"
        age = 21
        print(self.name)
        print(age)

    def f2(self):
        print(self.name)
        print(age)

emp1 = Employee()
emp1.f1()
emp1.f2()
'''

# special method
# __init__()
# constructor in python

'''
class Employee:
    def __init__(self):
        self.name = "Sam"

    def f2(self):
        print(self.name)

emp1 = Employee()
##emp1.f1()
emp1.f2()
'''


#
'''
class Employee:
    def __init__(self,first,last,address,phone):
        self.first = first
        self.last = last
        self.address = address
        self.phone = phone

    def fullName(self):
        return "{} {}".format(self.first,self.last)

    def HRteam(self):
        return "{} -> {}".format(self.fullName(),self.phone)

emp1 = Employee("sachin","kumar","delhi",998877)
emp2 = Employee("rohit","renil","pune",778899)

print(emp1.fullName())
print(emp2.fullName())
print(emp1.HRteam())
'''

#
'''
class Student:
    count = 0  # class attribute
    def __init__(self,name,fee):
        self.name = name
        self.fee = fee
        Student.count = Student.count + 1

    def fullDetails(self):
        return "{} -> {}".format(self.name,self.fee)

s1 = Student("sachin",1000)
s2 = Student("rohit",1200)
s3 = Student("virat",1300)

print(s1.fullDetails())
print("Total Students:",Student.count)
'''

# Inheritance
# 1 - direct inheritance
# A->B
'''
class A:
    def f1(self):
        print("f1 from class A")

class B(A):
    def f2(self):
        print("f2 from class B")

b = B()
b.f2()
b.f1()
'''

# 2 - Multilevel inheritance
# A -> B -> C
'''
class A:
    def f1(self):
        print("f1 from A")

class B(A):
    def f2(self):
        print("f2 from B")

class C(B):
    def f3(self):
        print("f3 from C")

c = C()
c.f3()
c.f2()
c.f1()
'''

# 3 Multiple inheritance

# A -> C <- B
'''
class A:
    def f1(self):
        print("f1 from A")

class B:
    def f2(self):
        print("f2 from B")

class C(A,B):
    def f3(self):
        print("f3 from C")

c = C()
c.f3()
c.f2()
c.f1()
'''

#
'''
class Vehicle:
    def generalUsage(self):
        print("General Usage: Transportation")


class Car(Vehicle):
    def __init__(self):
        print("I am a car")
        self.wheels = 4
        self.roof = True

    def specificUsage(self):
        print("Specific Usage: Vacation with family")

class Bike(Vehicle):
    def __init__(self):
        print("I am a Bile")
        self.wheels = 2
        self.roof = True

    def specificUsage(self):
        print("Specific Usage: Solo travel")

c = Car()
c.generalUsage()
c.specificUsage()
'''

# special methods or magic methods or dunder methods
# __init__()
'''
class Employee:
    def __init__(self,first,last,age,address,phone,salary):
        self.first = first
        self.last = last
        self.age = age
        self.address = address
        self.phone = phone
        self.salary = salary

    def fullName(self):
        return "{} {}".format(self.first,self.last)

    def __str__(self):
        return "{} -> {} -> {}".format(self.fullName(),self.age,self.address)

    def __add__(self,other):
        return self.salary + other.salary

'''
#

class StringOps:
    def __init__(self,str1):
        self.str1 = str1

    def countVowels(self):
        count = 0
        for i in self.str1:
            if i in "aeiouAEIOU":
                count += 1

        return count\

st1 = input("Enter a string:")
s1 = StringOps(st1)

print("Total Vowels:",s1.countVowels())

















    



















































        
















































































































































