#swap 2 num without using third variable


a=int(input("Enter First Number: "))
b=int(input("Enter Second Number: "))


a,b=b,a

print(a," ",b)