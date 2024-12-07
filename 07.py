with open(__file__[-5:-3]+'.in') as f: data = f.read()

lines = data.split("\n")

def canBeSolved(result,operators):
    
    res = []
    res2 = []
    
    for i,x in enumerate(operators):  
              
        res = res2.copy()
        res2 = []       
         
        if i == 0:
            res2.append(x)        
        else:
            for y in res:
                if y*x < result:
                    res2.append(y*x)
                elif y*x == result:
                    return True
                if y+x < result:
                    res2.append(y+x)
                elif y+x == result:
                    return True
                if int(str(y)+str(x))<result:
                    res2.append(int(str(y)+str(x)))              
                elif int(str(y)+str(x)) == result:
                    return True
    return False

p1=0
for line in lines:
    result = int(line.split(':')[0])
    operators = list(map(int,line.split(':')[1].split()))
    
    if canBeSolved(result,operators):
        p1+=result

print(p1)