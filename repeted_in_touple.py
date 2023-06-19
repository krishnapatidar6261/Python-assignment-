#Write a Python program to find the repeated items of a tuple. 

t=(1,2,3,2,4,5,3,6,7,8,9,4,3)
l=[]

for i in t:
    
    if t.count(i)>1 and i not in l:
        l.append(i)
        
print(l)