a=input("Enter a string: ")

upper=0
lower=0
space=0
char=0
for i in a:
    
    if i==i.upper():
        upper+=1
    elif i== i.lower():
        lower+=1
        
    
        
        
print("UPPER: ",upper)
print("Lower:",lower)
