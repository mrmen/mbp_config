#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import sys

if len(sys.argv)<3:
    sys.exit("Not enough argument.")
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
    res.append([0,0,0,0])
for line in resultats.readlines():
    L = line.split(";")[1:]
    for index in range(nombreComps):
        res[index][int(L[index])] += 1
resultats.close()


niveaux = "Insuffisant", "Fragile", "Satisfaisant", "Très satisfaisant"
couleurs = ["lightcoral", "gold", "yellowgreen", "lightskyblue"]
explode = (0, 0, 0, 0)

for index in range(nombreComps):
    plt.pie(res[index], explode=explode, labels=niveaux, colors=couleurs, 
        autopct='%1.1f%%', shadow=True, startangle=90)
    plt.title(competences[index])
    plt.axis('equal')
    plt.savefig(ds+"-"+classe+"-"+competences[index]+'.png')
    plt.clf()
