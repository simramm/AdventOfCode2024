import math
with open(__file__[-5:-3]+'.in') as f: data = f.read()
lines = data.split("\n\n")

rules = [list(map(int,x.split('|'))) for x in lines[0].split('\n')]
updates = [list(map(int,x.split(','))) for x in lines[1].split('\n')]

def isCorrect(update):
    correct = True
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[0]) > update.index(rule[1]):
                correct = False
                return correct           
    return correct

def correctOrder(update):
    newUpdate=[]
    for j,u in enumerate(update):
        if j == 0: newUpdate.append(u)
        for i,nu in enumerate(newUpdate):
            for rule in rules:
                if u==rule[0] and nu==rule[1] and u not in newUpdate:
                    newUpdate.insert(i,u)
        if u not in newUpdate:
            newUpdate.append(u)                  
    return newUpdate   
    
p1=0
p2=0

for update in updates:
            
    if isCorrect(update):        
        p1 += update[int(math.floor(len(update)/2))]
        
    if not isCorrect(update):   
        p2 += correctOrder(update)[int(math.floor(len(correctOrder(update))/2))]

print(p1)
print(p2)