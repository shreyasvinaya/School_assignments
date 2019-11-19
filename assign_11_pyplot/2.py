

import numpy as np
import matplotlib.pyplot as py
py.xlabel('Store Location')
py.ylabel('Count')
py.title('Most comman items sold by store location')
y=np.arange(0,2400,200)
x=np.array([1,2,3,4,5,6])
y=[[]]
citems=[[250,620,380,210,170,450],[203,204,120,345,190,275],[154,514,478,278,574,854],[485,745,759,482,459,458],[75,847,458,254,264,548],[548,698,547,584,265,454],[457,487,487,512,485,457]]
py.yticks(np.arange(0,2200,200))
py.bar(x-2.4,citems[0],color='g',width=.1)
py.bar(x-1.6,citems[1],color='b',width=.1)
py.bar(x-.8,citems[2],color='y',width=.1)
py.bar(x,citems[3],color='m',width=.1)
py.bar(x+.8,citems[4],color='r',width=.1)
py.bar(x+1.6,citems[5],color='c',width=.1)
py.bar(x-2.4,citems[0],color='k',width=.1)



py.show()




