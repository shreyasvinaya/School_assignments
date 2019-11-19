from getpass import *






def fread():
	pass
	f=open('S:/Senior Secondary/Our Generation.txt','r' )
	f.seek(0)
	a=f.readlines()
	f.close()
	g=open('reversePoem.txt','w')
	print(a)
	for i in range(len(a)):
		pass
		m=a[i]
		'''for j in range(len(m)):
			pass
			a[i][j],a[i][len(m)-j-1]=a[i][len(m)-j-1],a[i][j]'''
	
	a.reverse()

	print(a)
	
	g.writelines(a)
	g.close()
if __name__ == '__main__':
	pass
	fread()

def multiread():
	pass
	f=open('S:/Senior Secondary/fileNames.txt','r' )
	f.seek(0)
	a=f.readlines()
	f.close()

	m=[]
	for i in a:
		pass
		temp=list(i)
		del temp[-1]
		i=''.join(temp)
		print(i)
		f=open(i,'r')
		t=[]
		t.append(i)
		f.seek(0)
		t.append(len(f.read()))
		f.seek(0)
		a=0
		
		while f.readline():
			pass
			f.readline()
			a+=1
		t.append(a)
		m.append(t)
		f.close()
	for q in m:
		pass
		print('the file is:',q[0])
		print('it has',q[2],'lines')
		print('it has',q[1],'words')
	
if __name__ == '__main__':
	pass
	multiread()

def username_pass():
	pass
	#username=input('enter username')
	#password=input('enter password')
	user = getuser()
	p = getpass()

	while True: 
	    pwd = getpass("User Name : %s" % user) 
	  
	    if pwd == 'abcd': 
	        print "Welcome!!!"
	        break
	    else: 
	        print "The password you entered is incorrect."
	f=open()