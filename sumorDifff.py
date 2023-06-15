def check_values(a, b):
    if a == b or a + b == 5 or abs(a - b) == 5:
        return True
    else:
        return False

a=int(input("Enter First Number"))
b=int(input("Enter First Number"))
print(check_values(a,b))