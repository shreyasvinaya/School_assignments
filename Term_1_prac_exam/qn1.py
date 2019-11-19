#question 1
# program to define a stack of characters which form a string

def menu():
	pass

def push1(arr,e,top):
	pass
	if top>15 :
		pass
		print('overflow')
		a='overflow'
		return None
	else:
		arr.append(e)
		top+=1
		return [arr,top]
def pop1(arr,top):
	pass
	if top==0:
		pass
		top=None
	if top==None:
		pass
		print('underflow')
		return None
	else:
		q=arr.pop()
		top-=1
		return [q,arr,top]
'''if __name__=='__main__':
	pass
	test1=[1,2,3,4,5,6,7,8,9]
	print(push1(test1,10,len(test1)))
	print(pop1(test1,len(test1)))

'''
def pop_str(l1):
	pass
	m2=[]
	for x in range(0,len(l1)):
		m1=pop1(l1,len(l1))
		if m1==None:
			break
		t=m1[1]
		m2.append(m1[0])
	a=''
	for j in m2:
		pass
		a+=j
	print(a)
	#return a

def pushchr(str1):
	pass
	list1=[]
	for i in range(len(str1)):
		pass
		m=push1(list1,str1[i],len(list1))
	print(list1)
	return list1

a123=pushchr('qwerty')
pop_str(a123)
