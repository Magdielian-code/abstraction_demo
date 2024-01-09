# Duck Typing

class Duck:
    def swim(self):
        print("Ducks can swim.")
    def sound(self):
        print("Makes a quack-quack sound.")

class Dog:
    def swim(self):
        print("Dogs can swim.")
    def sound(self):
        print("Dogs bark.")

def display(duck):
    duck.swim()
    duck.sound()
    return "Information Displayed."

duck = Duck()
dog = Dog()

print(display(dog))


# Operator Overriding

class Demo:
    def __init__(self,r,i):
        self.real = r
        self.imaginary =i

    def __add__(self, other):
        return f"{self.real + other.real} + {self.imaginary + other.imaginary}i"
    
c1 = Demo(2,3)
c2 = Demo(4, 6)
print(c1 + c2)

# Method Overlaoding - Though not supported by python, there are other ways to go about it.

class AddDemo:
    def add(self, *args):
        total = 0
        for i in args:
            total += i
        return total
    
p1 = AddDemo()
print(p1.add(3,5,2,3))
print(p1.add(3,5,6,7,8,7,1,2,3))


# Mehtod Overriding - Happens often in Inheritance

class Father:
    def sleep(self):
        print("sleeps 5 hours a day.")
class Son(Father):
    def sleep(self):
        return "sleeps 3 hours a day."

Sam = Son()
print(Sam.sleep())