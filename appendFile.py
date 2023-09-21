# Write a Python program to append text to a file and display the text

with open("file.txt","a+") as f:
    
    a=f.write(" This line is appended")
    
    f.seek(0)
    print(f.read())
    
    
