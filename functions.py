#page with al the functions i will ever need\
import math

def testing1(x=10,y=15):
	pass
	sum1=x+y
	return (sum1)
	
def area_rect(l=1,b=1):
	pass
	area=l*b
	return area
def peri_rect(l=1,b=1):
	pass
	peri=2*(l+b)
	return peri
def multiply(*n,i1=-1):
	pass
	temp = 1
	for i in n:
		pass
		temp*=i
	return temp
def add(*n,i1=-1):
	pass
	temp = 0
	for i in n:
		pass
		temp+=i
	return temp
def addlist(lst,i1=0,i2=-1):
	pass
	if lst[i1] is lst[i2]:
		pass
		return lst[i1]
	else:
		pass
		return lst[i1] + addlist(lst,i1+1,i2)
def mullist(lst,i1=0,i2=-1):
	pass
	if lst[i1] is lst[i2]:
		pass
		return lst[i1]
	else:
		pass
		return lst[i1] * mullist(lst,i1+1,i2)
def cap_and_rev(st):
	pass
	a=' '.join(list(n[0].upper()+n[1:-1]+n[-1].upper() for n in st.split())[::-1])
	return a
	'''if  :
		pass
	else:
		pass
		n*multiply()'''

def pattern1(n=3):
	pass
	for a in range(1,n+1):
		pass
		for b in range(1,a+1):
			pass
			print('*',end="")

		print('\r')

def insertionSort(arr): 
	for i in range(1, len(arr)): 
		key = arr[i] 
		j = i-1
		while j >=0 and key < arr[j] : 
				arr[j+1] = arr[j] 
				j -= 1
		arr[j+1] = key 

def no_of(st):
	pass
	b=list(st)
	n=0
	c=0
	v=0
	sp=0
	normal=0
	vowels = ['a','e','i','o','u']
	for i in b:
		pass
		if i.isupper()==True:
			pass
			c+=1
		elif i.isdigit()==True :
			pass
			n+=1
		elif i in vowels :
			pass
			v+=1
		elif i.isalpha()==True:
			pass
			normal+=1
		else:
			sp+=1
	l=[n,c,v,sp,normal]
	return l

def power(a,n):
	pass
	if n==1:
		pass
		return a
	else:
		pass
		return a * power(a,n-1)

def multiples_of_7(n=10):
	pass
	
	if n==1:
		pass
		print(0)
		return 7
	else:
		pass
		print(n*7)
		return multiples_of_7(n-1)
def triangle(n):
    temp=[]
    
    if n==0:
        return []
    
    if n==1:
        return [[1]]
    
    else:
        Pascal_triangle=[[1]]
             
        for i in range(1,n):
            #print (i)
            for j in range(0,len(Pascal_triangle[i-1])):            
                #print (j)
                
                if j==0: 
                    temp.append(Pascal_triangle[i-1][0])
                    print (temp) 
            
                else:
                    temp.append(Pascal_triangle[i-1][j-1]+Pascal_triangle[i-1][j])
                    print (temp)
            temp.append(1)
            Pascal_triangle.append(temp)
            temp=[]
    
    return Pascal_triangle

def triangle1(n):
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        new_row = [1]
        result = triangle(n-1)
        last_row = result[-1]
        for i in range(len(last_row)-1):
            new_row.append(last_row[i] + last_row[i+1])
        new_row += [1]
        result.append(new_row)
    return result

