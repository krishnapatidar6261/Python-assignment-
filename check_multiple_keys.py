# Write a Python program to check multiple keys exists in a dictionary 

d1={
    1:"krishna",
    2:"aachal",
    3:"aashish",
    
}
d2={
    4:"hemant",
    5:"ritesh",
    "krishna":101,
    "aashish":102
}

d1.update(d2)
print(d1)