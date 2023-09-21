with open("file2.txt","r")as f:
    l1=""  
    while True:
        
        line=f.readline()
        #print(line)
        if line=="":
            break
        else:
            
            
            l1=l1+line
    print(l1)