from abc import ABC, abstractmethod
import turtle
class Shape:            #abstract class with abstract methods and concrete method.
    @abstractmethod
    def set_side(self):
        pass
    @abstractmethod
    def get_side(self):
        pass
    @abstractmethod
    def get_area(self):
        pass
    @abstractmethod
    def draw(self):
        pass
    def Fav(self):
        print("Square is my fav shape")

class Best:
    def best(self):
        print("I am better")

class Square(Shape, Best):
    def __init__(self, s = 0):
        self.side = s
    def set_side(self, s):
        self.side  = s
    def get_side(self):
        return  (self.side)
    def get_area(self):
        return (self.side * self.side)
    def draw(self):
        t = turtle.Turtle();
        t.forward(self.side)
        t.left(90)
        t.forward(self.side)
        t.left(90)
        t.forward(self.side)
        t.left(90)
        t.forward(self.side)
        t.left(90)
        turtle.done()
    def best(self):
        print("Square is best")

class Rectangle(Shape):
    def __init__(self, l = 0, w = 0):
        self.__length = l
        self.__width = w
    def set_side(self, l, w):
        self.length = l
        self.width  = w
    def get_area(self):
        return (self.length * self.width)
    def draw(self):
        t = turtle.Turtle()
        t.forward(self.length)
        t.left(90)
        t.forward(self.width)
        t.left(90)
        t.forward(self.length)
        t.left(90)
        t.forward(self.width)
        t.left(90)

class Circle(Shape):
    def __init__(self, r = 0):
        self.__radius = r
    def set_radius(self, r):
        self.radius = r
    def get_radius(self):
        return (self.radius)
    def find_area(self):
        pi = 3.14
        return (pi * self.radius * self.radius)
    def draw(self):
        t = turtle.Turtle()
        t.circle(self.radius)
        turtle.done()
class Hexagon(Shape):
    def __init__(self, n = 0, l = 0):
        self.num = n
        self.length = l
    def set_props(self, n, l):
        self.num = n
        self.length = l
    def draw(self):
        t = turtle.Turtle()
        angle = 360.0 / self.num

        for i in range(self.num):
            t.forward(self.length)
            t.right(angle)

        turtle.done()
class Heptagon(Shape):
    def __init__(self, s = 0):
        self.__side = s
    def set_side(self, s):
        self.side = s
    def get_side(self):
        return self.side
    def draw(self):
        t = turtle.Turtle()
        for i in range(7):
            t.forward(self.side)
            t.right(51.42)
        turtle.done()
class Octagon(Shape):
    def __init__(self, s = 0):
        self.__side = s
    def set_side(self, s):
        self.side = s
    def get_side(self):
        return self.side
    def draw(self):
        t = turtle.Turtle()
        for i in range(8):
            t.forward(self.side)
            t.right(45)
        turtle.done()
class Pentagon(Shape):
    def __init__(self, n = 0, l = 0):
        self.num = n
        self.length = l
    def set_props(self, n, l):
        self.num = n
        self.length = l
    def draw(self):
        t = turtle.Turtle()
        angle = 360.0 / self.num

        for i in range(self.num):
            t.forward(self.length)
            t.right(angle)

        turtle.done()
class Nanogon(Shape):
    def __init__(self, s = 0):
        self.__side = s
    def set_side(self, s):
        self.side = s
    def get_side(self):
        return self.side
    def draw(self):
        t = turtle.Turtle()
        for i in range(9):
            t.forward(self.side)
            t.right(40)
        turtle.done()


s = Square()
s.set_side(50)
s.draw()
s.Fav()
s.best()

