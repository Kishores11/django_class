# mime :- multipurpose internet mail extension

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

message = MIMEMultipart()
message["Subject"] = "Flipkart Big Billion Day Sale"
##message["Cc"] = "abc@gmail.com
##message["Bcc"] = "wre@gmail.com

message["From"] = "Flipkart Company"

# user amd pwd
username = input("Enter login email id:")
pwd = "dkcgzkhbloexbzlo"

#sender $ receiver
sender = username
##receiver = input("Enter receiver's email id:")

receiver = ["kishoresaravanan392@gmail.com","kishoresaravanan112@gmail.com"]

# mail body

body = """
<h1>BBD SALE </h1>
<h2>BUY 1 GET 2 FREE </h2>
<p>Last 2 days</p>
"""
txt = MIMEText(body,"html")  #string:- plain
message.attach(txt)


# attach an image
f = open("abc.jpg","rb") #rb:-read binary mode
img = MIMEImage(f.read())
message.attach(img)

server = smtplib.SMTP("smtp.gmail.com","587")
server.starttls()
print("-----server connected----")

server.login(username,pwd)
print("---Login Successfully--")

server.sendmail(sender,receiver,message.as_string())
print("---mail sent successfully----")
