'''5.	Consider a List of this manner:
[‘P001’,1.5]  This is the example of a list which holds  a process id and its CPU burst
Create a menu based program to emulate the FCFS process scheduling: Use dynamic queues.
i.	Add a process
ii.	Execute the process
iii.	Calculate throughput'''
import modq as m
p = []
t = []
thr = 0
rp = -1
fp = 0
rt = -1
ft = 0
while True:
    name = input('enter process name or e to exit ')
    if name == 'e':
        print('throughput =',thr)
        break
    else:
        time = int(input('enter CPU burst time '))
        rp,fp = m.enqueue(p,name,fp,rp)
        rt,ft = m.enqueue(t,time,ft,rt)
        thr += time

