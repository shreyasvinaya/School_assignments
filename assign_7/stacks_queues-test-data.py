#import numpy
from stacks_queues import *

empty_stk=[]
a=pop_list(empty_stk,0)
pushlist(empty_stk,78,len(empty_stk))
pushlist(empty_stk,99,len(empty_stk))
m=pop_list(empty_stk,1)
print(m)

stri='abcdef'
l1=list(stri)

m2=[]
for x in range(0,len(l1)):
	pass
	#print(x)
	m1=pop_list(l1,len(l1))
	if m1==None:
		pass
		break
	t=m1[1]
	m2.append(m1[0])

print(m2)



#binary
num = int(input('Enter a number'))

def binary(num):
	pass
	stk = []
	while num/2 > 0:
		if num%2 == 0:
			pushlist(stk,'0',len(stk))
		else:
			pushlist(stk,'1',len(stk))
		num //= 2
		stk = stk[::-1]
	binary = ''
	for i in stk:
		binary += i
	print(binary)
binary(num)

a='2*(5+4)-8/2'
print(toPostfix(list(a)))