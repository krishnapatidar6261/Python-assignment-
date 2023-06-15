def func(str,str2):
    
    halfstring= len(str)//2
    
    st1=str[:halfstring]
    st2=str[halfstring:]
    
    complete=st1+" "+str2+" "+st2
    print(complete)
    
str=input("Enter first String: ")
str2=input("Enter Second String: ")
func(str,str2)