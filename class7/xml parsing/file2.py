'''
from xml.dom.minidom import parse

f = parse("sample.xml")

catalog = f.documentElement
print("-"*30)
book = catalog.getElementsByTagName("book")
for i in book:
    print(i.getAttribute("id"))
    print("-"*30)
    a = i.getElementsByTagName("author")[0]
    print(a.childNodes[0].data)

    b = i.getElementsByTagName("title")[0]
    print(b.childNodes[0].data)

    c = i.getElementsByTagName("genre")[0]
    print(c.childNodes[0].data)

    d = i.getElementsByTagName("price")[0]
    print(d.childNodes[0].data)

    e = i.getElementsByTagName("publish_date")[0]
    print(d.childNodes[0].data)

    f = i.getElementsByTagName("description")[0]
    print(f.childNodes[0].data)

    print("-"*30)

'''

from xml.dom.minidom import parse
import csv
 
f = parse("sample.xml")
 
catalog = f.documentElement
 
book = catalog.getElementsByTagName("book")
 
f1 = open("book.csv","w",newline="")
obj = csv.writer(f1)
obj.writerow(["ID","Author","Title","Genre","Price","Publish Date","Description"])
 
for i in book:
    var = i.getAttribute("id")

    author = i.getElementsByTagName("author")[0]
    a = author.childNodes[0].data
 
    title = i.getElementsByTagName("title")[0]
    b = title.childNodes[0].data
 
    genre = i.getElementsByTagName("genre")[0]
    c = genre.childNodes[0].data
 
    price = i.getElementsByTagName("price")[0]
    d = price.childNodes[0].data
 
    publish_date = i.getElementsByTagName("publish_date")[0]
    e = publish_date.childNodes[0].data
 
    description = i.getElementsByTagName("description")[0]
    f = description.childNodes[0].data
 
    obj.writerow([var,a,b,c,d,e,f])
 
f1.close()
print("--- File Converted ---")


