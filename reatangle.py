#Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of 
# a rectangle

class rectangle:
    
    def __init__(self,length,width):
        
        self.l=length
        self.w=width
    
    def area(self):
        
        self.area=self.l*self.w
        
        print("Area of rectangle is: ",self.area)
        
ob=rectangle(
    int(input("Enter length of rectangle: ")),
    int(input("Enter Width of rectangle: "))
)
ob.area()