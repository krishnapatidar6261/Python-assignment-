s="Hello i am krishna patidar and patidar is my surname"
word=input("Enter word to count: ")
count=0
l=s.split()
for i in l:
    
    if word==i:
        count+=1
              
print(count)