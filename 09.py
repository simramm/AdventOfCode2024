with open(__file__[-5:-3]+'.in') as f: data = f.read()

blocks=[]
ids = []
id = 0
for i,c in enumerate(data):
    blocks.append(int(c))
    
    if int(i) %2 == 1:
    
        ids.append('.')
    else:
        ids.append(id)
        id +=1
         
i = 0
while True:
    if i+1>len(blocks):
        break
    
    if ids[-1] == '.':
        ids.pop()
        blocks.pop()
        i=0
    
    if ids[i] == '.':        
            if blocks[i] == blocks[-1]:
                ids[i] = ids[-1]                
                ids.pop()
                blocks.pop()
                
            elif blocks[i] > blocks[-1]:
                blocks[i] -=blocks[-1]     
                blocks.insert(i,blocks.pop())
                ids.insert(i,ids.pop())
                
            elif blocks[i] < blocks[-1]:                
                ids[i]=ids[-1]             
                blocks[-1] -=blocks[i] 
    i+=1

p1 = 0
ind = 0
for x,y in zip(blocks,ids):
    for z in range(1,x+1):
        p1 +=ind*y
        ind+=1
    
    
print(p1)

#### p2 starting over ####

pos=0
id=0
files = {}
blanks = {}

for i,c in enumerate(data):    
    if i % 2 == 1:
        blanks[pos]=int(c)
    else:
        files[id]=(pos,int(c))
        id+=1
    pos+=int(c)

for id,(start,size) in reversed(files.items()):    
    for bstart,bsize in sorted(blanks.items()):
        
        if bstart >= start:
            continue
        
        if size == bsize:
            files[id] = (bstart,size)
            del blanks[bstart]
            blanks[start]=size
            break         

        elif size < bsize:                        
            files[id]=(bstart,size)            
            del blanks[bstart]
            blanks[bstart+size]=bsize-size
            break

p2=0
for id,(start,size) in files.items():    
    for x in range(start,start+size):
        p2+=id*x
print(p2)