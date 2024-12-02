with open(__file__[-5:-3]+'.in') as f: data = f.read()
#with open(__file__[-5:-3]+'-test.in') as f: data = f.read()
lines = data.split("\n")

def isGood(row):
    diffs=[]
    for i in range(len(row)-1):
        diffs.append(row[i+1]-row[i])
    diffs.sort()
    if set(diffs).issubset({1,2,3}) or set(diffs).issubset({-3,-2,-1}):
        return True
    return False

p1=0

for line in lines:
    row = list(map(int,line.split()))
    if isGood(row):
        p1+=1
print(p1)

p2=0

for line in lines:
    row = list(map(int,line.split()))
    
    good = False
    
    for i in range(len(row)):
        row2 = row[:i]+row[i+1:]
        if isGood(row2):
            good = True
    if good:
        p2+=1
        good = False
            
print(p2)