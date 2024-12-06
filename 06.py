with open(__file__[-5:-3]+'.in') as f: data = f.read()
#with open(__file__[-5:-3]+'-test.in') as f: data = f.read()

lines = data.split("\n")

R = len(lines)
C = len(lines[0])

grid = []
for r in range(R):
    row=[]
    for c in range(C):
        if lines[r][c] =='^':
            gr = r
            gc = c
        row.append(lines[r][c])
    grid.append(row)
dr = -1
dc = 0

r = gr
c = gc

visited = {(r,c)}

while -1<r<R and -1<c<C:
    
    visited.add((r,c))    
    nr = r + dr
    nc = c + dc
    
    if -1<nr<R and -1<nc<C and grid[nr][nc]=='#':
        dc,dr = -dr,dc      
    r += dr
    c += dc
    
print(len(visited))

def createsLoop(grid,r,c):
    visited2 = set()
    
    dr = -1
    dc = 0
    visited2.add((r,c,dr,dc)) 
    while True:     

        visited2.add((r,c,dr,dc))
        
        nr = r + dr
        nc = c + dc
        
        if nr<0 or nr>=R or nc<0 or nc>=C:
            return False
        
        if grid[nr][nc]=='#':    
            dc,dr = -dr,dc
        
        r += dr
        c += dc
        
        if (r,c,dr,dc) in visited2:
            return True


p2=0
for (cr,cc) in visited:
    
    if cr == gr and cc == gc:
        continue
    
    grid[cr][cc] = '#'
    if createsLoop(grid,gr,gc):
        p2+=1
        print(p2)
    grid[cr][cc] = '.'
            
print(p2)