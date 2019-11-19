#most repeated word 
a=input('enter a sentence')
b=a.split()
print(b)
d={}
for i in range(len(b)):
	pass
	if b[i] not in d:
		d[b[i]]=1
	else:
		for j in d:
			pass
			if b[i]==j :
				pass
				d[b[i]]+=1
highest=0
item=''
for q in d:
	if d[q]>highest :
		pass
		highest=d[q]
		item=q
print(item,highest)