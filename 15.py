with open(__file__[-5:-3]+'.in') as f: data = f.read()
#with open(__file__[-5:-3]+'-test.in') as f: data = f.read()

wh,moves = data.split("\n\n")

warehouse = []
for x in wh.split('\n'):
    row = []
    for y in x:
        row.append(y)
    warehouse.append(row)

R = len(warehouse)
C = len(warehouse[0])

sr,sc = 0,0

for r in range(R):
    for c in range(C):
        if warehouse[r][c] == '@':
            sr,sc = r,c
            break

def moveBoxes(warehouse,r,c,d):
    i=1
    if d == 1:
        dr = 0
        dc = 1
    elif d == 2:
        dr = 0
        dc = -1
    elif d == 3:
        dr = -1
        dc = 0
    elif d == 4:
        dr = 1
        dc = 0

    if warehouse[r+dr][c+dc] == '.':
        warehouse[r+dr][c+dc] = '@'
        warehouse[r][c] = '.'
    elif warehouse[r+dr][c+dc] == '#':
        return warehouse,r,c
    elif warehouse[r+dr][c+dc] == 'O':
        while warehouse[r+i*dr][c+i*dc] == 'O':
            i+=1
        if warehouse[r+i*dr][c+i*dc] == '.':
            warehouse[r+i*dr][c+i*dc] = 'O'
            warehouse[r+dr][c+dc] = '@'
            warehouse[r][c] = '.'                
        elif warehouse[r+i*dr][c+i*dc] == '#':
            return warehouse,r,c       
    return warehouse,r+dr,c+dc

rr,rc = sr,sc
for move in moves:
    for m in move:                
        if m == '>':
            d = 1            
        elif m == '<':
            d = 2        
        elif m == '^':
            d = 3            
        elif m == 'v':
            d = 4        
        if m != '\n':
            warehouse,rr,rc = moveBoxes(warehouse,rr,rc,d)

p1=0
for r in range(R):
    for c in range(C):
        if warehouse[r][c] == 'O':
            
            p1+=(100*r+c)
print(p1)