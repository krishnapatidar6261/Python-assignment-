s=input("Enter a String: ")
a=s[-3:]
if len(s)<=3:
    
    print(s)
    
elif a=="ing":
    
    s=s.replace(s[-3:],"ly")
    print(s)
    
else:
    
    s=s+"ing"
    print(s)
    
  
      