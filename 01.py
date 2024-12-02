with open(__file__[-5:-3]+'.in') as f: data = f.read()
with open(__file__[-5:-3]+'-test.in') as f: data = f.read()

lines = [x.split() for x in data.split("\n")]

left = []
right = []

for x in lines:
    left.append(int(x[0]))
    right.append(int(x[1]))
    
left.sort()
right.sort()

p1=0

for l,r in zip(left,right):    
    p1 += abs(l-r)    
print(p1)

p2=0

for l in left:
    for r in right:
        if l==r:
            p2+=l
print(p2)