def traverse(l):
    for i in l:
        print(i)

def sort(k,p):
    while k<=l[p] and p>=0:
        l[p+1]=l[p]
        p-=1
    return p

def insertsort(l):
    for i in range(1,len(l)):
        key=l[i]
        ptr=i-1
        ptr=sort(key,ptr)
        l[ptr+1]=key
        
def insert(l,it):
    l.append(0)
    for i in range(len(l)):
        if it<=l[i]:
            j=i
            while i<len(l)-1:
                l[i+1]=l[i]
                i+=1
            l[j]=it
            
def delete(l,it):
    pos=l.index(it)
    u=len(l)-1
    while i<=u:
        l[i]=l[i+1]
        i+=1

def mergelist(a,b):
    aptr,bptr,c,ua,ub=0,0,[],len(a)-1,len(b)-1
    while aptr<=ua and bptr<=ub:
        if a[aptr]<=b[bptr]:
            c.append(a[aptr])
            aptr+=1
        else:
            c.append(b[bptr])
            bptr+=1
    while bptr<=ub:
         c.append(b[bptr])
         bptr+=1
    while aptr<=ua:
         c.append(a[aptr])
         aptr+=1
    c=c[::-1]
    return c


    
    
