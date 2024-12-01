import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__,"Input.txt"))

# if test needed
#f = open(os.path.join(__location__,"Input_test.txt"))

#data = f.read().split("\n")

#data = f.read().split()
#data = list(map(int, f.read().split('\n')))
#data = list(map(int, f.read().split(',')))
data = [x.split("   ") for x in f.read().split("\n")]

print(data)



left =[]
right = []

for x in data:
    left.append(int(x[0]))
    right.append(int(x[1]))
    


left.sort()
right.sort()


print(left)
print(right)

result=0
for l in left:
    for r in right:
        if l==r:
            result+=l
print(result)