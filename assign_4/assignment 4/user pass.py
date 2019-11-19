us=input('Username ')
pa=input('Password')
fo=open(r'user.txt')
users=fo.readlines()
a=False
for i in users:
    k=i.index('-')
    if us==i[:k]:
        a=True
        if i[k+1:len(i)-1]==pa:
            print('Verified')
        else:
            print('Wrong Pass')
fo.close()
fo=open(r'user.txt','a')
if a==False:
    fo.write(us+"-"+pa+"\n")
fo.close()
