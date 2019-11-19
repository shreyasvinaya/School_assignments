def pushlist(l,elem,top1):
	pass
	global top
	
	top=top1
	if top==None :
		pass
		top=0
	else:
		top+=1
	l.append(elem)

def pop_list(l,top1):
	pass
	global top
	if top1==0:
			pass
			top1=None
	top=top1
	
	if top==None :
		pass
		print('underflow')
	else:
		a=l.pop()
		top=len(l)-1
		if top==-1:
			pass
			top=None
		return [a,top]

if __name__ == '__main__':
	b=[1,2,3,4,5,6,7,8,9]
	pushlist(b,78,len(b))
	print(b)
	m=pop_list(b,9)
	print(m)
	print(b)


def isOperand(c):
	return c.isalpha()

def precedence(c):
	precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
	return precedence[c]

def isLeftParenthesis(c):
	if c=='(':
		pass
		return True

def isRightParenthesis(c):
	if c==')':
		return True

def hasLessOrEqualPriority(c,stk):
	try: 
		a = precedence(c) 
		b = precedence(stk[-1])
		return True if a  <= b else False
	except KeyError:  
		return False
def isEmpty(stk):
	return True if len(stk)==0 else False
	
def toPostfix(infix):
	stack = []
	postfix = ''
	for c in infix:
		if isOperand(c):
			postfix += c
		else:
			if isLeftParenthesis(c):
				stack.append(c)
			elif isRightParenthesis(c):
				operator = stack.pop()
				while not isLeftParenthesis(operator):
					postfix += operator
					operator = stack.pop()              
			else:
				while (not isEmpty(stack)) and hasLessOrEqualPriority(c,stack):
					postfix += stack.pop()
				stack.append(c)

	while (not isEmpty(stack)):
		postfix += stack.pop()
	print(postfix)
	return postfix


def infixToPostfix(exp): 
	stack = []
	postfix = ''
	for i in exp: 
		if isOperand(i): 
			postfix+=i 

		elif i  == '(': 
			pushlist(stk,i,len(stk)) 

		elif i == ')': 
			while( (not isEmpty(stk)) and stk[-1] != '('): 
				a = pop_list(stk,len(stk)) 
				postfix+=a
			if (not isEmpty(stk) and stk[-1] != '('): 
				return -1
			else: 
				postfix+=pop_list(stk) 

	else: 
		while(not isEmpty(stk) and self.notGreater(i)): 
			self.output.append(self.pop()) 
		self.push(i) 

	while not self.isEmpty(): 
		self.output.append(self.pop()) 

	print ("".join(self.output))