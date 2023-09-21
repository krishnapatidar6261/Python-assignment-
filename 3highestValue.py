# Write a Python program to find the highest 3 values in a dictionary 
d={
    1:2555,
    2:23000,
    3:34,
    4:22,
    5:22,
    "krishna":101,
    "aashish":102
}
l=[]

for i in d.values():
    
    l.append(i)
    
l.sort()
highest=l[:-4:-1]
print(highest)