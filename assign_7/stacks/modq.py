'''4.	Create a module which contains two function enqueue() and dequeue().
Enqueue accepts a list as a queue, its rear and front pointers and inserts an element into the queue.
Dequeue also receives the same parameters and deletes an element from the queue.'''
def enqueue(q,e,f,r):
    N = 44
    if r == -1:
        r = f = 0
        q.append(e)
        return f,r
    elif r == N - 1:
        print('overflow')
        return f,r
    else:
        q.append(e)
        r += 1
        return f,r
def dequeue(q,f,r):
    if r == -1:
        print('underflow')
        return f,r,None
    else:
         r -= 1
         f -= 1
         return f,r,q.pop()
