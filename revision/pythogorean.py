#pythogorean triplets
import math

a=int(input('enter the number till which you want pythogorean triplets'))
l=[]
for x in range(1,a):
	pass
	for y in range(1,x):
		pass
		m = ((x**2) + (y**2))**(1/2)
		if int(m)==m:
			pass
			l.append([x,y,m])

'''for d in range(len(l)):
	pass
	for s in range(len(l)):
		pass
		#print(l[d][2]==l[s][2])
		if int(l[d][2])==int(l[s][2]) :
			pass	
			#l.delete(s)
			#print(1)

'''

print(l)