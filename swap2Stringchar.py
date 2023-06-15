s1=input("Enter first String: ")
s2=input("Enter Second String: ")

a=s1.replace(s1[0:2],s2[0:2])
b=s2.replace(s2[0:2],s1[0:2])

print(a+" "+b)
