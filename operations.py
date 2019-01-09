#-*- coding:utf-8-*-
import sys
import urllib.parse
import urllib.request
from pathlib import Path
home = str(Path.home())

# xlop doc at
#
# https://ctan.math.illinois.edu/macros/generic/xlop/doc/xlop-doc-fr.pdf
#

def usage():
    print('''operations.py opérateurs nombre1 nombre2
opérateur peut être add, sub, mul ou div
nombre1 et nombre2 doivent être notés avec un «.» et pas une «,»

Le pdf est téléchargé sur le bureau sous le nom : operateurs-py.pdf
''')
    sys.exit(1)
    
if len(sys.argv)<4:
    usage()

op = sys.argv[1]
if not (sys.argv[1] in ["add","sub","mul","div"]):
    usage()
else:
    op = "\\op"+sys.argv[1]
n1,n2 = sys.argv[2],sys.argv[3]
    

base = "http://latexonline.cc/compile"
text = "\\documentclass{standalone}\\usepackage{xlop}\\begin{document}%s{%s}{%s}\\end{document}"%(op,n1,n2)
a=urllib.parse.quote_plus(text)
urllib.request.urlretrieve(base+"/?text="+a,home+"/Desktop/operations-py.pdf")
