l=0
w=0
fr=open("filenames.txt")
txt=fr.readline()
while(txt):
    l=l+1
    for i in txt.split():
        w=w+1
        
    print(l,w)
    txt=fr.readline()
    w=0

fr.close()    
