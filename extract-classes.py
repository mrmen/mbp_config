import sys, codecs
import clipboard

def pprint(text):
	clipboard.set(clipboard.get()+text)

clipboard.set('')
CLASSES = [str(niv)+'EME'+str(num) for niv in range(3,7) for num in range(1,7)]
CAT = [cat+age+sex for cat in ["B", "M", "C"] for age in ["1", "2"] for sex in ["F", "G"]]
FILE = 'dos.csv'

pprint('''\\documentclass{article}
\\usepackage[utf8]{inputenc}
\\usepackage[T1]{fontenc}
\\usepackage[margin=2cm]{geometry}
\\usepackage{fancyhdr, anyfontsize}
\\pagestyle{empty}
\\begin{document}
\\renewcommand{\\arraystretch}{3}
\\fontsize{35}{23}\\selectfont
''')
for i in CAT:
    for classe in CLASSES:
        file = codecs.open(FILE,'r', 'utf-8')
        string = ''
        count = 0
        pprint('%% '+i+'\n')
    #    pprint('\\fancyhead[C]{'+i+'}')
        for line in file.readlines():
            if (i in line) and (classe in line):
            	eleve = line.replace("\\n","").split(";")
            	string += "\\noindent\\begin{minipage}{0.5\\linewidth}\\begin{tabular}{|p{5cm}p{12cm}|}"
            	string += "\\hline\n"
            	string += "Nom :& %s\\\\"%eleve[1]
            	string += "Prénom :& %s\\\\"%eleve[2]
            	string += "Dossard :& %s\\\\"%eleve[0]
            	string += "Cat. :& %s (%s)\\\\"%(eleve[3],eleve[4])
            	string += "\\hline\\end{tabular}\\end{minipage}"
    
            	count +=1
            	if count%1==0:
            		string += "\n\n\\vfill\n\n"
            	if count == 2:
            		string += ""#\\newpage"
            		count = 0
        
        string += "\n\n\\newpage\\newpage"
        pprint(string)
        file.close()
pprint('\\end{document}')

