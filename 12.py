with open(__file__[-5:-3]+'.in') as f: data = f.read()

lines = data.split("\n")
R = len(lines)
C = len(lines[0])

areas = []
done = set()

for r in range(R):
    for c in range(C):
        area = set()
        if (r,c) not in done:
            area.add((r,c))
            done.add((r,c))     
            while True:
                le = len(area)                
                for plot in area.copy():                    
                    pr,pc = plot                       
                    if pr<R-1 and lines[pr+1][pc] == lines[pr][pc]:
                        area.add((pr+1,pc))
                        done.add((pr+1,pc))
                    if pc<C-1 and lines[pr][pc+1] == lines[pr][pc]:
                        area.add((pr,pc+1))
                        done.add((pr,pc+1))
                    if 0<pr and lines[pr-1][pc] == lines[pr][pc]:
                        area.add((pr-1,pc))
                        done.add((pr-1,pc))
                    if 0<pc and lines[pr][pc-1] == lines[pr][pc]:
                        area.add((pr,pc-1))
                        done.add((pr,pc-1))
                if le == len(area):
                    break
            areas.append(area)
        
def perimeter(area):    
    p=0    
    for a in area:
        n=0        
        ar,ac = a        
        if (ar+1,ac) in area:
            n+=1
        if (ar,ac+1) in area:
            n+=1
        if (ar-1,ac) in area:
            n+=1
        if (ar,ac-1) in area:
            n+=1        
        p+=4-n   
    return p

def corners(area): 
    s=0
    for a in area:
        c=0        
        ar,ac = a
        # outside
        if (ar+1,ac) not in area and (ar,ac+1) not in area:
            c+=1
        if (ar+1,ac) not in area and (ar,ac-1) not in area:
            c+=1
        if (ar-1,ac) not in area and (ar,ac+1) not in area:
            c+=1
        if (ar-1,ac) not in area and (ar,ac-1) not in area:
            c+=1
        # inside
        if (ar+1,ac) in area and (ar+1,ac+1) not in area and (ar,ac+1) in area:
            c+=1
        if (ar+1,ac) in area and (ar+1,ac-1) not in area and (ar,ac-1) in area:
            c+=1
        if (ar-1,ac) in area and (ar-1,ac+1) not in area and (ar,ac+1) in area:
            c+=1
        if (ar-1,ac) in area and (ar-1,ac-1) not in area and (ar,ac-1) in area:
            c+=1        
        s+=c
    return s

p1,p2=0,0
for area in areas:    
    p1+= len(area) * perimeter(area)
    p2+= len(area) * corners(area)
print(p1)
print(p2)