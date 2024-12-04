with open(__file__[-5:-3]+'.in') as f: data = f.read()
lines = data.split()

R = len(lines)
C = len(lines[0])

cw = []

for r in range(R):
    row=[]
    for c in range(C):
       row.append(lines[r][c])
    cw.append(row)
    
    
p1 = 0
for y,r in enumerate(cw):
    for x,c in enumerate(cw[y]):
        
        if c =='X':

            if int(x) < C-3 and cw[y][x:x+4]==['X','M','A','S']:
                p1+=1
            if int(x) > 2 and cw[y][x-1] == 'M' and cw[y][x-2] == 'A' and cw[y][x-3] == 'S':
                p1+=1
            if int(y) < R-3 and cw[y+1][x] == 'M' and cw[y+2][x] == 'A' and cw[y+3][x] == 'S':
                p1+=1
            if int(y) > 2 and cw[y-1][x] == 'M' and cw[y-2][x] == 'A' and cw[y-3][x] == 'S':
                p1+=1            
            if int(y) < R-3 and int(x) < C-3 and cw[y+1][x+1] == 'M' and cw[y+2][x+2] == 'A' and cw[y+3][x+3] == 'S':
                p1+=1
            if int(y) < R-3 and int(x) > 2 and cw[y+1][x-1] == 'M' and cw[y+2][x-2] == 'A' and cw[y+3][x-3] == 'S':
                p1+=1
            if int(y) > 2 and int(x) < C-3 and int(x) < C-2 and cw[y-1][x+1] == 'M' and cw[y-2][x+2] == 'A' and cw[y-3][x+3] == 'S':
                p1+=1
            if int(y) > 2 and int(x) > 2 and cw[y-1][x-1] == 'M' and cw[y-2][x-2] == 'A' and cw[y-3][x-3] == 'S':
                p1+=1
                
print(p1)

p2 = 0

for y,r in enumerate(cw):
    for x,c in enumerate(cw[y]):
        
        if c =='M':
            if int(y) < R-2 and int(x) < C-2 and cw[y+1][x+1] == 'A' and cw[y+2][x+2] == 'S':
                if (cw[y][x+2] == 'M' and cw[y+2][x] =='S') or (cw[y][x+2] == 'S' and cw[y+2][x] =='M'):
                    p2+=1             
            if int(y) < R-2 and int(x) >1 and cw[y+1][x-1] == 'A' and cw[y+2][x-2] == 'S':
                if (cw[y][x-2] == 'M' and cw[y+2][x] =='S') or (cw[y][x-2] == 'S' and cw[y+2][x] =='M'):
                    p2+=1
            if int(y)>1 and int(x) < C-2 and cw[y-1][x+1] == 'A' and cw[y-2][x+2] == 'S':
                if (cw[y][x+2] == 'M' and cw[y-2][x] =='S') or (cw[y][x+2] == 'S' and cw[y-2][x] =='M'):
                    p2+=1
            if int(y)>1 and int(x)>1 and cw[y-1][x-1] == 'A' and cw[y-2][x-2] == 'S':
                if (cw[y][x-2] == 'M' and cw[y-2][x] =='S') or (cw[y][x-2] == 'S' and cw[y-2][x] =='M'):
                    p2+=1
print(p2/2)