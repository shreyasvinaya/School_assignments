fr=open(r"Z:\class 12\assignment 4\Our Generation.txt")
fw=open(r"Z:\class 12\assignment 4\reversePoem.txt","w")

txt=fr.readlines()
txt1=txt[::-1]

for i in txt1:
    if i==txt1[len(txt1)-1]:
        continue
    else:
        fw.write(i)
fr.close()
fw.close()
