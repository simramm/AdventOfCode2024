with open(__file__[-5:-3]+'.in') as f: data = f.read()

p1=0
p2=0

enabled = True
for i,c in enumerate(data):   
     
    if data[i:i+2] =='do':        
        if data[i+2:i+7] == "n't()":
            enabled= False
        if data[i+2:i+4] == "()":
            enabled= True   
                  
    if data[i:i+4] == 'mul(':
        x=''
        y=''
        j=i+4
        
        while data[j].isnumeric():
            x+=data[j]
            j+=1
            
        if data[j]==',':
            j+=1 
            
            while data[j].isnumeric():                
                y+=data[j]
                j+=1
                                
            if data[j]==')':
                p1+=int(x)*int(y)
                
                if enabled == True:
                    p2+=int(x)*int(y)
            
        
print(p1)
print(p2)