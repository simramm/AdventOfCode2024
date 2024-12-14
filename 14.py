with open(__file__[-5:-3]+'.in') as f: data = f.read()
R = 103
C = 101

# with open(__file__[-5:-3]+'-test.in') as f: data = f.read()
# R = 11
# C = 7

lines = [x.replace('p=','').replace('v=','').split() for x in data.split("\n")]

mr = R//2
mc = C//2

def calculateSafety(robots):
    q1,q2,q3,q4 =0,0,0,0
    for r,c,dr,dc in robots:        
        if r<mr and c<mc:
            q1+=1
        elif r>mr and c<mc:
            q2+=1
        elif r>mr and c>mc:
            q3+=1
        elif r<mr and c>mc:
            q4+=1
    return q1*q2*q3*q4

def moveRobots(robots,seconds):
    robotsnew = []
    for rob in robots:
        r,c,dr,dc = rob
        nr = (r + dr*seconds) % R
        nc = (c + dc*seconds) % C
        robotsnew.append((nr,nc,nr,dc))
    return robotsnew  

startrobots = []
for l in lines:
    r = 0
    c = 0
    dr = 0
    dc = 0
    c,r = map(int,l[0].split(','))
    dc,dr = map(int,l[1].split(','))
    startrobots.append((r,c,dr,dc))

minScore = 99999999999999
p2=0
for s in range(12000):
    robots = moveRobots(startrobots,s)
    
    if s == 100: #p1
        print(calculateSafety(robots))
    
    if calculateSafety(robots) < minScore:
        minScore = min(minScore,calculateSafety(robots))
        p2=s
        
        grid = [[' ' for c in range(C)] for r in range(R)]         
        for ro in robots:
            grid[ro[0]][ro[1]] = 'X'
            
print(p2)

# show the tree
for x in grid:
            line=''
            for y in x:
                line+=str(y)
            print(line)