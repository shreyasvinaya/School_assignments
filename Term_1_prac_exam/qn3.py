import mysql.connector as my

con=my.connect(host='localhost',user='root',passwd='root',database='shreyas')
cursor=con.cursor()
a=input('enter department')
sql1='select * from teachers where department =\''+ a +'\';'
cursor.execute(sql1)
data=cursor.fetchall()
if data==[]:
	pass
	print('No recods available')
for i in data:
	pass
	#print(i)
	for k in i:
		pass
		if i.index(k)==1:
			pass
			print(k,end=((10-len(k))*' '))
		else:
			print(k,end=(5*' '))

	print(' ')

con.close()