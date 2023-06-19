d={
    1:"krishna",
    2:"aashish",
    3:"aashish",
    4:"hemant",
    5:"krishna",
    "krishna":101,
    "aashish":102
}
l=[]
for i in d.values():
    
    if i not in l:
        
        l.append(i)
print(l)