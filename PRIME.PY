n=int(input("Entyer Number: "))

if n==2:
    print("prime")

else:
    for i in range(2,n):
        if n%i == 0:
            print("not prime")
            break
    else:
        print("prime")