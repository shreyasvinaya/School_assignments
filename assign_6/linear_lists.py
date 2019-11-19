import datetime,bisect

def traverse(l):
	for i in l:
		print(i)

def insertionSort(arr): 
	for i in range(1, len(arr)): 
		key = arr[i] 
		j = i-1
		while j >=0 and key < arr[j] : 
				arr[j+1] = arr[j] 
				j -= 1
		arr[j+1] = key

def binarySearch(arr, l, r, x):
	while l <= r: 
		mid = l + (r - l)//2
		if arr[mid] == x: 
			return mid 
		elif arr[mid] < x: 
			l = mid + 1
		else: 
			r = mid - 1
	return -1





def sort(k,p):
	while k<=l[p] and p>=0:
		l[p+1]=l[p]
	return p

def insertsort(l):
	for i in range(1,len(l)):
		key=l[i]
		ptr=i-1
		ptr=sort(key,ptr)
		l[ptr+1]=key
        
def insert(l,item):
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

def binarySearch_rec(arr, l, r, x): 
	if r >= l: 
		mid = l + (r - l)//2
		if arr[mid] == x: 
			return mid 
		elif arr[mid] > x: 
			return binarySearch(arr, l, mid-1, x) 
		else: 
			return binarySearch(arr, mid + 1, r, x) 

	else: 
		return -1

def lin_search(arr,x):
	pass
	ctr=0
	while ctr<len(arr):
		pass
		if arr[ctr]==x:
			pass
			return ctr
			break
		else:
			ctr+=1
	if ctr>=len(arr):
		pass
		return -1


def insort_my(list1,element):
	pass
	result1 = binarySearch(list1, 0, len(list1)-1, element)
	if result1 != -1: 
		print ("Element is present at index " ,result1)
	else: 
		#print ("Element is not present in array")
		insert(list1,element)
		print('the element is now added')
		result1 = binarySearch(list1, 0, len(list1)-1, element)
		if result1 != -1: 
			print ("Element is present at index " ,result1)

def transpose_matrix(a):
	pass
	#b=[ [a[x][y],a[x-1][y]] for y in range(len(a[0])) for x in range(1,len(a)) ]
	c=[ [a[x][y] for x in range(len(a))] for y in range(len(a[0]))  ]
	print(c)

def url_edit():
	pass
	l=['http://www.dasfk.com','www.try.com', 'www.google.com']
	b=[(i if 'http://' == i[:7] else 'http://'+ i) for i in l]
	print(b)


if __name__ == '__main__':
	'''arr = [1,2,3,4,10,40,50,76,89,90,100,150,200,450] 
	x = 40
	time_bin_init=datetime.datetime.now()
	result1 = binarySearch(arr, 0, len(arr)-1, x) 
	if result1 != -1: 
		print ("Element is present at index " ,result1)
	else: 
		print ("Element is not present in array")
	time_bin_final=datetime.datetime.now()
	print('time taken by normal binary search is:',time_bin_final - time_bin_init)


	time_bin_rec_init=datetime.datetime.now()
	result2 = binarySearch_rec(arr, 0, len(arr)-1, x) 
	if result2 != -1: 
		print ("Element is present at index " ,result2)
	else: 
		print ("Element is not present in array")
	time_bin_rec_final=datetime.datetime.now()
	print('time taken by recursive binary search is:',time_bin_rec_final - time_bin_rec_init)

	time_lin_init=datetime.datetime.now()
	result3 = lin_search(arr, x) 
	if result3 != -1: 
		print ("Element is present at index " ,result3)
	else: 
		print ("Element is not present in array")
	time_lin_final=datetime.datetime.now()
	print('time taken by Linear search is:',time_lin_final - time_lin_init)
	insort_my(arr,45)'''
	matrix1=[[12,35],[23,45],[56,34],[7,8]]
	matrix2=[[12,35,23,45],[56,34,7,8],[78,45,199,999]]
	transpose_matrix(matrix2)
	url_edit()