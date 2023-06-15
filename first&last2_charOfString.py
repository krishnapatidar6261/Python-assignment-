s=input("Enter String: ")

if len(s)<2:
    
    print("Empty String: ")
    
else:
    
    first=s[:2]
    second=s[-2:]
    
    print(first+second)