import sys

d = ""
for _ in range(len(sys.argv)-1):
	d += sys.argv[_+1]

for _ in ["[", "{",]:
	d = d.replace(_,"")
e = d.split("}")
e.pop()
e[0] = "\"" + e[0]
mydict = {}
for _ in e:
	temp = []
	first_pass = _[1:].split(",")
	id = first_pass[0].split(":")[1].replace("\"","")
	name = first_pass[2].split(":")[1].replace("\"","")
	mydict[name] = id

for key in mydict:
	print(key + " : " + mydict[key])	

	



