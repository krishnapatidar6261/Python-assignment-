n=int(input("How many line you want to read: "))
with open("file2.txt","r") as f:
    
    for i in range(n):
        
        print(f.readline())