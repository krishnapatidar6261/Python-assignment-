n=int(input("Enter Number to check Prime Number or NOT: "))

if n==1:
    print("Number is Not Prime Number") 
else:    
    if n==2:
        print("Number is Prime")
    else:
        if n==3:
            print("Number is Prime Number")
        else:
            for i in range(3,(n//2)+1,2):
            
                if n%i==0:
                    print("Number is Not Prime ")
                    break
            else:
                print("Number is Prime")