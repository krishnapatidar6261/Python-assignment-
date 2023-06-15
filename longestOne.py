def longest(l):
   # l=["hemant","jakspal","oooooooo"]

    length=0

    for i in l:

        if length<len(i):

            length=len(i)
        else:
            print(length)
            
            break

longest(l=["Krishna","aashis","Jaspal"])