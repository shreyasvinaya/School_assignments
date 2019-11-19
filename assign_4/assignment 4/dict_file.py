import pickle
max=0
def max1(txt):
    global max
    for i in txt:
        if txt[i]>max:
            max=txt[i]
        
fo=open("sample.dat","wb")
d1=eval(input("enter dict 1"))
d2=eval(input("enter dict 2"))
pickle.dump(d1,fo)
pickle.dump(d2,fo)
fo.close()

fr=open("sample.dat","rb")
txt=pickle.load(fr)
while(txt):
    max1(txt)
    try:
        txt=pickle.load(fr)
    except:
        txt=False
fr.close()
    
print(max)
for j in d1:
    if d1[j]==max:
        print(j)

for x in d2:
    if d2[x]==max:
        print(x)
        









































































































