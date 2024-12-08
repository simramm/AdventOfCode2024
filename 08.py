with open(__file__[-5:-3]+'.in') as f: data = f.read()
#with open(__file__[-5:-3]+'-test.in') as f: data = f.read()

lines = data.split("\n")

R = len(lines)
C = len(lines[0])

antennas = []

for r in range(R):
    row=[]
    for c in range(C):
        if lines[r][c] != '.':
            antennas.append([lines[r][c],r,c])

antinodesp1 = set()
antinodesp2 = set()

for a in antennas:    
    for b in antennas:        
        if a[0] == b[0] and not a == b:
            
            diffr = b[1]-a[1]
            diffc = b[2]-a[2]
            
            newan1r=b[1]+diffr
            newan1c=b[2]+diffc
            
            if 0<=newan1r<R and 0<=newan1c<C:
                antinodesp1.add((newan1r,newan1c))
            
            newan2r=a[1]-diffr
            newan2c=a[2]-diffc
            
            if 0<=newan2r<R and 0<=newan2c<C:
                antinodesp1.add((newan2r,newan2c))       
                           
for a in antennas:    
    for b in antennas:        
        if a[0] == b[0] and not a == b:
            
            diffr = b[1]-a[1]
            diffc = b[2]-a[2]
            
            newan1r=b[1]
            newan1c=b[2]           
            
            while 0<=newan1r<R and 0<=newan1c<C:                
                antinodesp2.add((newan1r,newan1c))
                newan1r+=diffr
                newan1c+=diffc
                
            newan2r=a[1]
            newan2c=a[2]
    
            while 0<=newan2r<R and 0<=newan2c<C:                
                antinodesp2.add((newan2r,newan2c))
                newan2r-=diffr
                newan2c-=diffc  
                                     
print(len(antinodesp1))
print(len(antinodesp2))


