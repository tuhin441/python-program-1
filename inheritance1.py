class shape(): #shape is inherited, here shape is call parent or super class.
    def __init__(self,dim1,dim2):
        self.dim1=dim1
        self.dim2=dim2
    
    def area(self):
        print("I am area method of shape class")

class triangle(shape): #shape is inherited, here shape is call parent or super class.
    def area(self):
        area = 0.5* self.dim1 * self.dim2
        print("Area of triangle : ", area)

class rectangle(shape):  # triangle&rectangle is called subclass or child class.
    def area(self):
        area = self.dim1 * self.dim2
        print("Area of rectangle : ", area)

t1 = triangle(10,20)
t1.area()
R1 = rectangle(30,50)
R1.area()