#infix to postfix
import mods as m
s=input("Enter your expression")
l=list(s)
print(l)
d={"0":0,"/":4,"*":3,"+":2,"-":1}
l1=[]
top=len(l1)
print(top)
for a in l:
    if a not in ("-","+","*","/","(",")"):#(ord(a)>=65 and ord(a)<=90) or (ord(a)>=97 and ord(a)<=122)or(a=="1" or "2" or"3"or"4"or"5"or"6"or"7"or"8"or"9"):
        print(a,end="")
    if a in ("-","+","*","/"):
        print('t',top)
        while (top!=0)and(d[a]<=d[l1[top-1]]) and (l1[top-1]!="("):
            p=stacks.pull(l1,top)
            top=len(l1)
            print(p[1],end="")
            m.push(l1,a,top)
        top=len(l1)

    if a=="(":
        m.push(l1,a,top)
        top=len(l1)
    if a==")":
        while l1[top]!="(":
            m=m.pull(l1)
            print(m[1],end="")
        l=m.pull(l1)
print(top)
while top!=0:
    x=stacks.pop(l1)
    print(x[1])
                       
                       
        

        
        
        
