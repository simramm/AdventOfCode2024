import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__,"Input.txt"))

data = list(map(int, f.read()))
pixels = [2]*150

for i,n in enumerate(data):
    
    p = i % (25*6)
    if pixels[p] == 2:
        if n == 0:
            pixels[p] ='█'
        if n == 1:
            pixels[p] =' '

row =''

for i,p in enumerate(pixels):
    
    if i % (25)==0:
        print(row)
        row=''    
    row+=p
print(row)