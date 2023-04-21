import json

#writing

f=open("source.txt","w")
data={101:{"name":"sam","salary":10000},102:{"name":"john","salary":20000}}
json.dump(data,f,indent=4)
f.close()

#reading

f=open("source.txt")
var=json.load(f)
print(var)
f.close()

      
