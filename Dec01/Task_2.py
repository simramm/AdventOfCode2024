import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__,"Input.txt"))

data = [x.split("   ") for x in f.read().split("\n")]

left =[]
right = []

for x in data:
    left.append(int(x[0]))
    right.append(int(x[1]))
    
left.sort()
right.sort()

result=0
for l in left:
    for r in right:
        if l==r:
            result+=l
print(result)