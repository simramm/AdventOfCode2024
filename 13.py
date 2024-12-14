with open(__file__[-5:-3]+'.in') as f: data = f.read()
lines = [x.split("\n") for x in data.split("\n\n")]

machines = []
for l in lines:
    a = tuple(map(int,l[0].replace('Button A: X+','').replace(' Y+','').split(',')))
    b = tuple(map(int,l[1].replace('Button B: X+','').replace(' Y+','').split(',')))
    p = tuple(map(int,l[2].replace('Prize: X=','').replace(' Y=','').split(',')))    
    machines.append([a,b,p])

def Solve(machines,x):
    res=0
    for m in machines:
    # linear algebra magic https://en.wikipedia.org/wiki/Cramer's_rule#Explicit_formulas_for_small_systems
    # m[0][0]x + m[1][0]y = m[2][0] and m[0][1]x + m[1][1]y = m[2][1]
        a = ((m[2][0]+x)*m[1][1]-m[1][0]*(m[2][1]+x))/(m[0][0]*m[1][1]-m[1][0]*m[0][1])
        b = (m[0][0]*(m[2][1]+x)-(m[2][0]+x)*m[0][1])/(m[0][0]*m[1][1]-m[1][0]*m[0][1])
        if a == int(a) and b== int(b):
            res+=int(3*a+b)
    return res        

print(Solve(machines,0))
print(Solve(machines,10000000000000))