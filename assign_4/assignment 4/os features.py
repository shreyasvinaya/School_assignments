fw=open(r"osFeatures.txt",'r')
fr=open(r"features.txt",'w')
txt=fw.readline()
while txt:
    if txt[0] in 'iaw':
        fr.write(txt[0:len(txt)-2]+'#\n')
    txt=fw.readline()
fw.close()
fr.close()
        
