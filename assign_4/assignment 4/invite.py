l=eval(input('Enter list '))
fo=open(r'guests.txt','w')
for i in l:
    fo.write(i+"\n")
fo2=open(r'invitations.txt','w')
fo3=open(r'letter.txt','r')
let=fo3.read()
for i in l:
    x=let.replace('Friend',i)
    fo2.write(x+"\n")
fo.close()
fo2.close()
fo3.close()
