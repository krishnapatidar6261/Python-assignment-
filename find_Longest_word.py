with open("file3.txt","r") as f:
    l1=[]
    
    while True:
        
        line=f.readline()
        
        if line=="":
            break
        
        else:
            
            l=line.split()
            l1.extend(l)
    print(l1)
            
length=0           
for i in l1:
    
    if length<len(i):
        
        length=len(i)
        
    
print(length)
             