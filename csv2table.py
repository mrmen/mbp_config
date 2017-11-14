#!/usr/bin/env python3
#-*-coding:utf-8-*-

import sys

if len(sys.argv)!=2:
    sys.exit(1)

file = open(sys.argv[1],"r")
Content = []
for line in file.readlines():
    Content.append(line.split(";"))
file.close()

max_size = [0 for i in range(len(Content[0]))]
for element in Content:
    for i in range(len(element)):
        max_size[i] = max(max_size[i],len(element[i]))
for element in Content:
    for i in range(len(element)):
        element[i] = element[i] + " "*(max_size[i]-len(element[i]))

toadd = []
for nb in max_size:
    toadd.append("-"*nb)
toadd[len(toadd)-1] += "\n"
Content.append(toadd)
Content.insert(0,toadd)

output = []
for _ in Content:
    output.append(" ".join(_))
print("".join(output))

