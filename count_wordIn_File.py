word=input("Enter Word to count: ")
l1=[]
with open("file2.txt","r")as f:
    
    
    a=f.read()
    print(a.count(word))
    