import pickle as pl

def menu():
	pass
	inp=input('\n\na)Add New teacher \nb)Report of all Teachers \nEnter Your choice:')
	if inp=='a':
		pass
		savefile()
	elif inp=='b':
		report1()
	else:
		print('please enter valid input')
		menu()

def savefile():
	pass
	name1=input('enter teacher name')
	age=int(input('enter teacher age'))
	dep=input('enter department')
	dat123=input('enter date of admission(YYYY-MM-DD format please)')
	sal=int(input('enter salary'))
	gen=input('enter gender(single char only)')
	data=[name1,age,dep,dat123,sal,gen]
	with open('teachers.dat','ab+') as f1:
		pl.dump(data,f1)
		'''
		qwe1=['Sangeeta',35,'Computer','1999-07-01',40000,'F']
		qwe2=['Jugal',34,'Computer','1997-01-10',12000,'M']
		qwe3=['Sharmila',31,'History','1998-03-24',20000,'F']
		qwe4=['Sandeep',32,'Math','1996-12-12',30000,'M']
		qwe5=['Sangeeta',35,'History','1999-07-01',40000,'F']
		pl.dump(qwe1,f1)
		pl.dump(qwe2,f1)
		pl.dump(qwe3,f1)
		pl.dump(qwe4,f1)
		pl.dump(qwe5,f1)'''
		print('data stored')
		
	menu()

def report1():
	pass
	gen=input('enter gender')
	data1=[]
	with open('teachers.dat','rb') as f1:
		b=0
		while True:
			pass
			try :
				pass
				a=pl.load(f1)
				data1.append(a)
			except :
				print('The required data is: ')
				break
	for i in data1:
		pass
		#print(i)
		if i[5]==gen:
			pass
			for k in i:
				pass
				if i.index(k)==0 or i.index(k)==2:
					pass
					print(k,end=((15-len(k))*' '))
				else:
					print(k,end=(5*' '))

			print(' ')
	menu()

menu()



