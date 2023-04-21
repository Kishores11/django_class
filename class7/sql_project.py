# SQL Project

import sqlite3
import csv
import smtplib

# create a DB
db = sqlite3.connect("DB_Proj.sqlite")

# create a Table
try:
    db.execute("""create table student(
                    Roll integer,
                    Name text,
                    Math integer,
                    Science integer,
                    Computer integer)""")
except:
    pass

def newStudent():
    print("--- Add A New Student Here ---")

    list1 = []
    roll = int(input("Enter roll number:"))
    list1.append(roll)
    name = input("Enter name:")
    list1.append(name)
    m = int(input("Enter marks in Math:"))
    list1.append(m)
    s = int(input("Enter marks in Science:"))
    list1.append(s)
    c = int(input("Enter marks in Computer:"))
    list1.append(c)

    db.execute("insert into student values(?,?,?,?,?)",list1)
    db.commit()
    print("--- Student Addedd Successfully ---")

def checkResult():
    print("---- Check your result here ----")
    cursor = db.cursor()
    r = int(input("Enter your roll number to check your result:"))
    cursor.execute("select * from student where Roll = ?",[r])
    var = cursor.fetchall()
    print(var) # [(1,"sam",87,45,56)]

    print("-"*30)
    print("Roll Number:",var[0][0])
    print("Name:",var[0][1])
    print("Math:",var[0][2])
    print("Science:",var[0][3])
    print("Computer:",var[0][4])

    perc = (var[0][2]+var[0][3]+var[0][4])/3
    print("Percentage: %.2f"%perc)
    print("-"*30)
    return perc

def genReport():
    cursor = db.cursor(self,perc)
    cursor.execute("select * from student")
    var = cursor.fetchall()
    print(var)
    # [(1, 'sam', 98, 67, 56), (2, 'john', 21, 45, 56), (3, 'mike', 87, 45, 67)]
    
    # write this data into csv file
    f = open("report.csv","w",newline="")
    obj = csv.writer(f)
    obj.writerow(["Roll","Name","Math","Science","Computer","Perc","Status"])

    for i in var:
        perc = "%.2f" %((i[-1]+i[-2]+i[-3])/3)
        if i[-1]>35 and i[-2]>35 and i[-3]>35:
            status = "PASS"
        else:
            status = "FAIL"
            
        list1 = list(i)
        list1.append(perc)
        list1.append(status)

        obj.writerow(list1)

    f.close()
    print("---- Report Generated Successfully ----")

def sendReport():
    server = smtplib.SMTP("smtp.gmail.com","587")  # server address, port number
    server.starttls()  # to make a secure connection
    print("--- Connected with the server ---")

    # login

    username = "kishoresaravanan392@gmail.com"
    pwd = "dkcgzkhbloexbzlo"
    server.login(username,pwd)
    print("--- Login Successfull ---")

    # send mail
    
    p = checkResult()
    print(p)
    sender = username
    receiver = input("Enter student's email id:")
    msg = "Percentage "+ str(p)
    server.sendmail(sender,receiver,msg)
    print("-- Mail sent successfully --")

while True:
    print("1. Add A New Student")
    print("2. Check Your Result")
    print("3. Generate Report In CSV Format")
    print("4. Send Report")
    print("5. Exit")
    ch = int(input("Enter your choice:"))

    if ch == 1:
        newStudent()
    elif ch == 2:
        checkResult()
    elif ch == 3:
        genReport()
    elif ch == 4:
        sendReport()
    elif ch == 5:
        print("-- Bye --")
        break
    else:
        print("-- Invalid Choice --")
