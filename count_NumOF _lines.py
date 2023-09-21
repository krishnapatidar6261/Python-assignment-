with open("file2.txt","r")as f:
    count=0   
    while True:
        
        line=f.readline()
        if line=="":
            break
        else:
            
            count=count+1
    print(count)