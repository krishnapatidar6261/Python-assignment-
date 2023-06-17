l=["krishna","aashish","naman","udu","aashtha","a","p","patidar","om","aa"]
c=[]
for i in l:
    
    if len(i)>=2:
      
        first=i[0]
        last=i[-1]  
        if first==last:
            
            c.append(i)
      
print(len(c))