#Write a Python function that takes two lists and returns true if they have at least one common member. 

def l(l1,l2):
    
    for i in l1:
        
        if i in l2:
            return True
        
      
l1=[1,2,3,5,6,7]
l2=[7,8,9,0]   
print(l(l1,l2))

