class circle:

    def __init__(self,r):

        self.r=r

    def radious(self):

        self.area=3.14*self.r*self.r

    def perimeter(self):

        self.p= 2*3.14*self.r

    def display(self):

        print("Area of circle is: ",self.area)
        print("perimeter of crcle is: ",self.p)

ob=circle(int(input("Enter radious of circle: ")))
ob.radious()
ob.perimeter()
ob.display()
