#Write a Python function to get the largest number, smallest num and sum of all from a list

n=int(input("How many Element you insert in the list: "))
l=[]
for i in range(n):
    inputt=int(input("Enter List Element: "))
    l.append(inputt)
    
l.sort()

greater=l[-1]
smaller=l[0]
print("Samller Number in list:",smaller)
print("Greater Number in list",greater)

sum=0
for i in l:
    
    sum=sum+i
    
print(sum)

