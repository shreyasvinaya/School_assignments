#validate.py

import random, math
from random import shuffle
from datetime import *

def verify_email(n):
	s=n.split('.')
	domain=s[-1]
	print(domain)
	first=''
	loc=0
	for i in s:
		pass
		if '@' in i :
			pass
			first=i.split('@')
			#print(first)
			s+=first
	if '@' not in s :
		pass
	for l in range(len(s)):
		pass
		#print(s[l])
		if "@" in s[l]:
			pass
			loc=l

		#print(s)
	s.remove(s[loc])
	#print(s)

	if len(domain)<5 and len(domain)>0  :
		pass
		print('your email is valid')
	else:
		pass
		print('your email is invalid')
		
if __name__ == '__main__' :
	pass
	verify_email(input('enter email'))

def generateOTP(n=4):
	pass
	digits = "0123456789"
	OTP = ""
	for i in range(n):
		pass
		OTP+=digits[random.randrange(10)]
	return OTP

if __name__ == '__main__' :
	pass
	print("OTP of 4 digits:", generateOTP())

def captcha(n=6):
	pass
	captcha=''
	spl='!@#$%^&*><?~'
	digits = "0123456789"
	alphabets='qwertyuiopasdfghjklzxcvbnm'
	caps='QWERTYUIOPASDFGHJKLZXCVBNM'
	temp1='1234'
	temp=''
	for i in range(n-3):
		pass
		temp=temp1[random.randrange(4)]
		if temp == '1' :
			pass
			captcha+=spl[random.randrange(len(spl))]
		elif temp =='2' :
			pass
			captcha+=digits[random.randrange(len(digits))]
		elif temp =='3' :
			pass
			captcha+=alphabets[random.randrange(len(alphabets))]
		else:
			pass
			captcha+=caps[random.randrange(len(caps))]
	captcha+=alphabets[random.randrange(len(alphabets))]
	captcha+=digits[random.randrange(len(digits))]
	captcha+=caps[random.randrange(len(caps))]
	captcha=list(captcha)
	print(captcha)
	shuffle(captcha)
	s=''
	captcha=s.join(captcha)
	print(captcha)
	return captcha

'''if __name__ == "__main__" : 
	pass
	a=captcha()
	print(a)
	b=input('enter the captcha here:')
	if str(a)==str(b) :
		pass
		print('you have been granted access')
	else:
		print('pls try again')
		captcha()
'''

def current_time():
	pass
	now = datetime.now()
	l=[]
	l.append(now.hours,now.minutes,now.date)
	nyc = now-timedelta(hours=9,minutes=30)
	syn
	print(nyc)
def menu():
	pass
	a=int(input('enter 1 or 2 or 3 bases on prg'))
	if a==1 :
		pass
		print("OTP of 4 digits:", generateOTP())
	elif a==2:
		pass
		
