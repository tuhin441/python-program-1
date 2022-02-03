from abc import ABC,abstractmethod


class shape():
    def __init__(self,dim1,dim2):
        self.dim1=dim1
        self.dim2=dim2
    @abstractmethod
    def area(self):
        pass

class Triangle(shape):
    def area(self):
        area = 0.5*self.dim1*self.dim2
        print("The area of Triangle is :", area)

class Rectangle(shape):
    def area(self):
        area = self.dim1*self.dim2
        print("This is area of Rectangle:",area)

p = Triangle(20,15)
p.area()

q = Rectangle(30,15)
q.area()

        