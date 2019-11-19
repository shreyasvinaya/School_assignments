import mods as m
e = input('enter an expression')
st = []
top = 0
op = {1:['^'],2:['%','*'],3:['+','-']}
for i in e:
    for j in op.values():
        
