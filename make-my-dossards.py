#!/usr/bin/env python
#-*-coding:utf-8-*-

import sys
if len(sys.argv)<=1:
    print("Pas de fichier en entree...")
    sys.exit(1)
if not "csv" in sys.argv[1]:
    print("Pas de fichier avec une extension csv en entree...")
    sys.exit(1)

file = open(sys.argv[1],"r")

string = '''\\documentclass{article}
\\usepackage[utf8]{inputenc}
\\usepackage[T1]{fontenc}
\\usepackage[margin=2cm]{geometry}
\\pagestyle{empty}
\\begin{document}
\\renewcommand{\\arraystretch}{3}
'''

count = 0

for line in file.readlines():
    eleve = line.replace("\\n","").split(";")
    string += "\\begin{minipage}{0.5\\linewidth}\\begin{tabular}{|p{4cm}p{4cm}|}"
    string += "\\hline\n"
    string += "Nom :& %s\\\\"%eleve[1]
    string += "Prénom :& %s\\\\"%eleve[2]
    string += "\\Huge{Dossard }:& \\Huge{%s}\\\\"%eleve[0]
    string += "Cat. :& %s\\\\"%eleve[3]
    string += "\\hline\\end{tabular}\\end{minipage}"

    count +=1
    if count%2==0:
        string += "\n\n"
    if count == 8:
        string += "\\newpage"
        count = 0
    
string += "\\end{document}"

print(string)
