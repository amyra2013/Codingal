class Rectangle():
    def __init__(self, l, w):
        self.l=l
        self.w=w
    def area(self):
        print("The length of the rectangle is {} units.".format(self.l))       
        print("The breadth of the rectangle is {} units.\n".format(self.w))
        area=self.l*self.w
        print("The area of the rectangle is {} square units.".format(area))

rec=Rectangle(15, 7)

rec.area()
