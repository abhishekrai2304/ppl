from abc import ABC, abstractmethod

class Animals(ABC):                             #abstract class with both abstract methods and concrete method.
    def __init__(self, color = "", legs = 0):
        self.color = color
        self.legs = legs
    def animals(self):
        print("I love animals")
    @abstractmethod
    def set_properties(self, c, l):
        pass
    def get_properties(self, name):
        pass

class Interface(ABC):       #class with only abstract methods are called interface class.
    @abstractmethod
    def eats(self):
        pass
    @abstractmethod
    def life(self):
        pass


class Fav:
    def myFav(self):
        print("I love Cats")


class Elephant(Animals, Fav):                        #hierarchical inheritance
    def __init__(self, c = "", l = 0):
        super().__init__(c, l)
    def set_properties(self, c, l):
        self.color = c
        self.legs = l
    def get_properties(self, name):
        print(name, "has", self.color, "color and", self.legs, "legs")
    def myFav(self):    #virtual method.  Overriding myFav method of the class Fav. Showing Polymorphism.
        print("I love Elephants")

class Dog(Animals):
    def __init__(self, c="", l=0):
        super().__init__(c, l)

    def set_properties(self, c, l):
        self.color = c
        self.legs = l

    def get_properties(self, name):
        print(name, "has", self.color, "color and", self.legs, "legs")

class Cat(Animals):
    def __init__(self, c="", l=0):
        super().__init__(c, l)

    def set_properties(self, c, l):
        self.color = c
        self.legs = l

    def get_properties(self, name):
        print(name, "has", self.color, "color and", self.legs, "legs")

class Tiger(Animals):
    def __init__(self, c="", l=0):
        super().__init__(c, l)

    def set_properties(self, c, l):
        self.color = c
        self.legs = l

    def get_properties(self, name):
        print(name, "has", self.color, "color and", self.legs, "legs")

class Lion(Animals):
    def __init__(self, c="", l=0):
        super().__init__(c, l)

    def set_properties(self, c, l):
        self.color = c
        self.legs = l

    def get_properties(self, name):
        print(name, "has", self.color, "color and", self.legs, "legs")
class Rabbit(Animals):
    def __init__(self, c="", l=0):
        super().__init__(c, l)

    def set_properties(self, c, l):
        self.color = c
        self.legs = l

    def get_properties(self, name):
        print(name, "has", self.color, "color and", self.legs, "legs")

class Penguin(Animals):
    def __init__(self, c="", l=0):
        super().__init__(c, l)

    def set_properties(self, c, l):
        self.color = c
        self.legs = l

    def get_properties(self, name):
        print(name, "has", self.color, "color and", self.legs, "legs")
class Dolphin(Animals):
    def __init__(self, c="", l=0):
        super().__init__(c, l)

    def set_properties(self, c, l):
        self.color = c
        self.legs = l

    def get_properties(self, name):
        print(name, "has", self.color, "color and", self.legs, "legs")
class Monkey(Animals):
    def __init__(self, c="", l=0):
        super().__init__(c, l)

    def set_properties(self, c, l):
        self.color = c
        self.legs = l

    def get_properties(self, name):
        print(name, "has", self.color, "color and", self.legs, "legs")
class Giraffae(Animals):
    def __init__(self, c="", l=0):
        super().__init__(c, l)

    def set_properties(self, c, l):
        self.color = c
        self.legs = l

    def get_properties(self, name):
        print(name, "has", self.color, "color and", self.legs, "legs")


e = Elephant()
e.set_properties("grey", 4)
e.get_properties("Elephant")
e.myFav();

g = Giraffae()
g.set_properties("yellow", 4)
g.get_properties("Giraffe")
