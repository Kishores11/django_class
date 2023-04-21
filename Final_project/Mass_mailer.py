import sqlite3
import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

db = sqlite3.connect("Student_Database.sqlite")

try:
    db.execute("""create table student(
                    Roll integer,
                    Name text,
                    Email text,
                    Math integer,
                    Science integer,
                    Computer integer)""")
except:
    pass
    
def addStudent():
    print("-------Add A New Student Here--------")

    list1 = []
    roll = int(input("Enter roll number:"))
    list1.append(roll)
    name = input("Enter name:")
    list1.append(name)
    email = input("Enter email id:")
    list1.append(email)
    maths = int(input("Enter marks in maths:"))
    list1.append(maths)
    science = int(input("Enter marks in science:"))
    list1.append(science)
    computer = int(input("Enter marks in computer:"))
    list1.append(computer)

    db.execute("insert into student values(?,?,?,?,?,?)",list1)
    db.commit()
    print("---Student Added Successfully----")

def checkResult():
    print("----Check Your Result Here-----")
    cursor = db.cursor()
    r = int(input("Enter your roll no to check your result:"))
    cursor.execute("select * from student where Roll = ?",[r])
    var = cursor.fetchall()
    print("-"*30)
    print("Roll Number:",var[0][0])
    print("Name:",var[0][1])
    print("Email:",var[0][2])
    print("Math:",var[0][3])
    print("Science:",var[0][4])
    print("Computer:",var[0][5])

    perc = (var[0][3]+var[0][4]+var[0][5])/3
    print("Percentage: %.2f"%perc)
    print("-"*30)

def generateReport():
    cursor = db.cursor()
    cursor.execute("select * from student")
    var = cursor.fetchall()
    f = open("student_report.csv","w",newline="")
    obj = csv.writer(f)
    obj.writerow(["Roll","Name","Email","Maths","Science","Computer","Perc","Status"])

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
    username=""    #enter the sender email id here
    pwd=""         #enter the password here
    sender=username
    subject="Result"
    
    with open('student_report.csv', mode='r') as f:
        reader = csv.reader(f)
        next(reader)
        for i in reader:
            text="Maths "+i[3]+"\n"+"Science "+i[4]+"\n"+"Computer "+i[5]+"\n"+"Percentage "+i[6]+"\n"+"Status :"+i[7]
            # print(text)
            receiver=i[2]
            msg=MIMEMultipart()
            msg["From"]=username
            msg["To"]=receiver
            msg["Subject"]=subject
            msg.attach(MIMEText(text,"plain"))
            text=msg.as_string()

            server=smtplib.SMTP("smtp.gmail.com","587")  
            server.starttls()
            server.login(username,pwd)
            server.sendmail(sender,receiver,text)
        
    print("-- Mail sent successfully --")

    

while True:
    print("******** MAIN MENU *********")
    print("\n1. Add A New Student\n2. Check Your Result\n3. Generate Report In CSV Format\n4. Send Report\n5. Exit")
    ch = int(input("Enter Your Choice:"))
    if ch == 1:
        addStudent()
    elif ch == 2:
        checkResult()
    elif ch == 3:
        generateReport()
    elif ch == 4:
        sendReport()
    elif ch == 5:
        break
    else:
        print("----Invalid Choice----")
        
    
