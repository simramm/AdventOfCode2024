with open(__file__[-5:-3]+'.in') as f: data = f.read()

lines = data.split("\n")

R = len(lines)
C = len(lines[0])

grid = []
for r in range(R):
    row=[]
    for c in range(C):
        row.append(int(lines[r][c]))
    grid.append(row)

def calculateScore(grid,r,c):
    positions = [(r,c)]        
    for x in range (1,10):
        positionsnew = []
        for r,c in positions:
            
            if r<R-1 and grid[r+1][c]==x:
                positionsnew.append((r+1,c))
            if c<C-1 and grid[r][c+1]==x:
                positionsnew.append((r,c+1))            
            if r>0 and grid[r-1][c]==x:
                positionsnew.append((r-1,c))                
            if c>0 and grid[r][c-1]==x:
                positionsnew.append((r,c-1))
        positions = positionsnew.copy()    
    return len(set(positions))

def calculateRating(grid,r,c):
    paths = [[(r,c)]]       
    for x in range (1,10):
        pathsnew = []        
        for path in paths:
            pathnew = path.copy()
            r,c = path[-1]
            
            if r<R-1 and grid[r+1][c]==x:
                pathnew.append((r+1,c))
                pathsnew.append(pathnew)
                pathnew = path.copy()
            if c<C-1 and grid[r][c+1]==x:
                pathnew.append((r,c+1))
                pathsnew.append(pathnew)
                pathnew = path.copy()            
            if r>0 and grid[r-1][c]==x:
                pathnew.append((r-1,c))
                pathsnew.append(pathnew)
                pathnew = path.copy()                
            if c>0 and grid[r][c-1]==x:
                pathnew.append((r,c-1))
                pathsnew.append(pathnew)
                pathnew = path.copy()
        paths = pathsnew.copy()
    return len(paths)

p1=0
p2=0
for r in range(R):
    for c in range(C):        
        if grid[r][c] == 0:
            p1+=calculateScore(grid,r,c)
            p2+=calculateRating(grid,r,c)
print(p1)
print(p2)