def fun(s):
    

    l=len(s)
    if l%4==0:

        s=s[-1:-len(s)-1:-1]
        print(s)

    else:
        print("String length does not divide by 4")

s=input("Enter String: ")
fun(s)