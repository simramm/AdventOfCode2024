with open(__file__[-5:-3]+'.in') as f: data = f.read()
stones = list(map(int, data.split(' ')))

numbers = {}
for s in stones:
    if s in numbers.values():
        numbers[s]+=1
    else:
        numbers[s] = 1
        
def blink(x,numbers):
    for z in range(x):        
        numbersnew = {}
        for k,v in numbers.items():
            l = len(str(k))
            if k == 0:
                if 1 in numbersnew.keys():
                    numbersnew[1] +=v
                else:
                    numbersnew[1] =v       
            elif l%2 == 0:
                if int(str(k)[:l//2]) in numbersnew.keys():
                    numbersnew[int(str(k)[:l//2])] += v
                else:
                    numbersnew[int(str(k)[:l//2])] = v
                if int(str(k)[l//2:]) in numbersnew.keys():
                    numbersnew[int(str(k)[l//2:])] += v
                else:
                    numbersnew[int(str(k)[l//2:])] = v
            else:                
                if k*2024 in numbersnew.keys():
                    numbersnew[k*2024] +=v
                else:
                    numbersnew[k*2024] =v                
        numbers = numbersnew.copy()
        if z == 24:
            numbers1 = numbersnew.copy()
    res=0
    for k,v in numbers.items():
        res+=v
    return res
    
print(blink(25,numbers))
print(blink(75,numbers))