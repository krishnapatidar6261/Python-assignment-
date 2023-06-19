#Write a Python script to print a dictionary where the keys are numbers between 1 and 15 and value are multiple of key

d={}

for i in range(1,16):
    
    d[i]=i*i
    
print(d)