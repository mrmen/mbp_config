#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import sys

def usage():
    print('''Usage :
comp2chart.py ds-name class-name

Files eleves.csv and comp.csv must be present.
The program should return png files according to previous files.
''')
    sys.exit(1)

    
if len(sys.argv)<3:
    usage()

ds=sys.argv[1]
classe=sys.argv[2]

resultats = open("eleves.csv","r")
comps = open("comp.csv","r")

competences = []
nombreComps = 0
for line in comps.readlines():
    competences.append(line.split(";")[0])
    nombreComps += 1
comps.close()

res = []
for _ in range(nombreComps):
    res.append([0,0,0,0,0])
for line in resultats.readlines():
    temp = line
    temp = temp.replace("\n", "").replace("	", ";").replace("\"", "").replace("\r", "").replace("	", ";")
    temp = temp.replace("Maîtrise insuffisante", "0")
    temp = temp.replace("Maîtrise fragile", "1")
    temp = temp.replace("Maîtrise satisfaisante", "2")
    temp = temp.replace("Très bonne maîtrise", "3")
    temp = temp.replace("Absent", "4")
    temp = temp.replace("Non évalué", "4")
    if "X;X" in temp:
       continue
    if "Élève" in temp:
       continue
    L = temp.split(";")[1:]
    for index in range(nombreComps):
        res[index][int(L[index])] += 1
resultats.close()


niveaux = "Insuffisant", "Fragile", "Satisfaisant", "Très satisfaisant", "Néant"
couleurs = ["lightcoral", "gold", "yellowgreen", "lightskyblue", "gray"]
explode = (0, 0, 0, 0, 0)

for index in range(nombreComps):
    plt.pie(res[index], explode=explode, labels=niveaux, colors=couleurs, 
        autopct='%1.1f%%', shadow=True, startangle=90)
    plt.title(competences[index])
    plt.axis('equal')
    plt.savefig(ds+"-"+classe+"-"+competences[index]+'.png')
    plt.clf()
