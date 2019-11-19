#2. Import the file into another program, send a string in the form of a stack. Reverse the string using pop.
#3. Using the same file convert a decimal number into  its binary equivalent using the stack functionality
import mods as m
#s = 'hellooo'
def rev(s):
  st = []
  top = 0
  for i in s:
    top = m.push(st,i,top)
  #print('top =',top)
  rev = []
  top1 = None
  for i in range (top+1):
    top,e = m.pull(st,top)
    top1 = m.push(rev,e,top1)
  #print(''.join(rev))
  #print('top1=',top1)
  return ''.join(rev)

st1 = []
top2 = 0
n = int(input('enter number'))
while n >= 1:
    top2 = m.push(st1,str(n%2),top2)
    n = n//2
print(st1)
print(rev(''.join(st1)))






































