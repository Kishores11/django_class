#xml parsing
'''
import xml.etree.ElementTree as et
f = et.parse("source.xml")

root = f.getroot()

#tag, attrib, text

#print(root.tag)
#print(root.attrib)

##print(root[1].tag)
##print(root[1].attrib)

print(root[2][0].tag)
print(root[2][0].text)
'''

from xml.dom.minidom import parse

f = parse("source.xml")

collection = f.documentElement
print(collection.getAttribute("about"))
print("-"*30)
element = collection.getElementsByTagName("element")
for i in element:
    print(i.getAttribute("screen"))
    print("-"*30)
    mname = i.getElementsByTagName("mname")[0]
    print(mname.childNodes[0].data)

    mtype = i.getElementsByTagName("mtype")[0]
    print(mtype.childNodes[0].data)

    duration = i.getElementsByTagName("duration")[0]
    print(duration.childNodes[0].data)

    print("-"*30)

    

