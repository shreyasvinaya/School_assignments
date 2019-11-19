'''3.	Imagine that you are writing a program for a simple text editor. Using stacks how would you implement the undo and redo options?
[consider a list as the text. Undo is the
deletion of the latest character into the text and redo is pushing it back in].'''
import mods as m
st = []
u = []
topu = 0
top = 0
flag = 0
#print('welcome to text editor!( enter < and press enter to undo or enter > and press enter to redo OR just press enter to exit)')
while True:
    n = input()
    for i in n:
        top = m.push(st,i,top)
    top,i = m.pull(st,top)
    #if i == '\n':
        #print('ahhhhhh')
        #top,e = m.pull(st,top)
        #topu = m.push(u,e,topu)
        #flag = 1
    if i == '<':
            if top == None:
                print('cannot undo')
            else:
                top,e = m.pull(st,top)
                topu = m.push(u,e,topu)
                flag = 1
    elif i == '>':
            if flag == 1:
                topu,e = m.pull(u,topu)
                top = m.push(st,e,top)
            else:
                print('cannot redo')
    elif i == '|':
            flag == "!"
    else:
        flag = 0
        top = m.push(st,i,top)
        top = m.push(st,'\n',top)   
    print(''.join(st))

    if flag == '!':
        break
    
            



























        
        
    
    
    
