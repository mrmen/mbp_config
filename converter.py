com = {0:0,1:1,2:1,3:2,4:2,5:3}
cal = {0:0,1:0,2:1,3:1,4:2,5:2,6:3,7:3}
mod = {0:0,1:1,2:1,3:2,4:2,5:3}
rai = {0:0,1:0,2:1,3:1,4:1,5:2,6:2,7:3,8:3}

fichier = open("bb.csv","r")
output = open("bb-3eme1.csv","w")
for line in fichier.readlines():
    name = " ".join(line.split(";")[0:2])
    pos = [name]
    s = line.replace("\n","").split(";")[4:]
    for comp,val in zip([com,cal,mod,rai], s):
        pos.append(str(comp[int(val)]))
    output.write(";".join(pos) + "\n")

fichier.close()
output.close()
