from applescript import asrun, asquote
import sys
import time

cmd = 'tell application "Fantastical" to parse sentence %s add immediately true'
print(sys.argv[1])

file = open(sys.argv[1],"r")
for line in file.readlines():
    print("adding :")
    print(line.replace("\n",""))
    asrun(cmd%asquote(line.replace("\n","")))
    time.sleep(1)
file.close()
