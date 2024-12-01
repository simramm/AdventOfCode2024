import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__,"Input.txt"))

# if test needed
#f = open(os.path.join(__location__,"Input_test.txt"))

#data = f.read().split("\n")

#data = f.read().split()
#data = list(map(int, f.read().split('\n')))
#data = list(map(int, f.read().split(',')))
#data = [x.split("\n") for x in f.read().split("\n\n")]


data = list(map(int, f.read()))


print(len(data))

layers = []

layer = 0

z = 0
o = 0
t = 0
    

for i,n in enumerate(data):
        
    if n == 0:
        z+=1
    if n == 1:
        o+=1
    if n ==2:
        t+=1
    
    if i % (25*6) ==0 and i !=0:
        layers.append([z,o*t])
        z,o,t = 0,0,0



omin=99999

result=0
print(len(layers))
for l in layers:    
    print(l)
    if l[0]<omin:
        omin=l[0]
        result=l[1]
    
print(omin,result)