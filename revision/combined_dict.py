#combine two dictionaries adding values for common keys

a=eval(input('enter dictionary 1 here'))
b=eval(input('enter dictionary 2 here'))


for j in b:
	pass
	if j in a :
		pass
		a[j]+=b[j]
	else:
		pass
		a[j]=b[j]

print(a)
