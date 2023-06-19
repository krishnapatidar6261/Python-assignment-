d={
    1:"krishna",
    2:"aachal",
    3:"aashish",
    4:"hemant",
    5:"ritesh",
    "krishna":101,
    "aashish":102
}
c=input("Enter key for check: ")

if c in d.keys() or int(c) in d.keys():
    print("Key exists")
    
else:
    print("key does not exits")