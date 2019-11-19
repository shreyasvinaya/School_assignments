'''1.	Create a file that implements the push and pop function of the stack.
Send the list and the top as parameters. Push should insert the element,
change the list and top value. Boundary conditions should be checked.
Pop should return the top value and delete an element. Print the deleted element.
1.	Import the file into another program, Send a stack of
i.	Empty stack of integers for popping
ii.	Push 2 elements into the stack
iii.	Pop 1 element of the stack
2.	Import the file into another program, send a string in the
        form of a stack. Reverse the string using pop.
2.	Using the same file  convert a decimal number
        into its binary equivalent using the stack functionality'''
def push(st,e,top):
    
    bound = 6688
    if top == bound:
        print('overflow')
        return top
    else:
        
          top = top + 1
          st.append(e)
          return top


def pull(st,top):
    if top == None:
        print('underflow')
        return top
    else:
        top -= 1
        return top,st.pop()

