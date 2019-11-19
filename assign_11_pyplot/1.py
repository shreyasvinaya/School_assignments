#pyplot 1st program

import numpy as np
import matplotlib.pyplot as py
py.xlabel('Days')
py.ylabel('\'000s ')
py.title('Visits to two new music sites on the web')
z=np.arange(1,16)
y=np.array([40,20,60,20,25,30,22,40,20,30,25,120,110,125,70])
x=np.array([120,118,120,100,35,75,35,45,40,110,150,82,80,165,170])
py.plot(z,y,'b',marker='s',markersize=3, markeredgecolor='blue')
py.plot(z,x,'r',marker='s',markersize=3, markeredgecolor='red')
py.xticks(np.arange(1,16))
py.yticks(np.arange(0,200,20))
py.grid()
py.show()