with open("file2.txt","r")as f:
    l1=[]   
    while True:
        
        line=f.readline()
        #print(line)
        if line=="":
            break
        else:
            
            l=line.split()
            l1.extend(l)
    print(l1)