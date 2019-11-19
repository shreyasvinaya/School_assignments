import mods as m
st = []
top = 0
top = m.push(st,8,top)
print(st)
print(top)
top = m.push(st,9,top)
print(st)
print(top)
top,poop = m.pull(st,top)
print(st)
print(top)
print('poop=',poop)
