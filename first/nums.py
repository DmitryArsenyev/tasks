def plus(a,b):
    return a + b

def mul(a,b):
    return a*b

def minus(a,b):
    return a - b

def delit(a,b):
    return a / b

print(2)

class Mammal:
    def move(self):
        print('Двигается')

class Hare(Mammal):
    def move(self):
        print('Прыгает')

animal = Mammal()
animal.move() # Двигается
hare = Hare()
hare.move()


class Parent():
    def __init__(self):
        print('Parent init')

    def method(self):
        print('Parent method')

class Child(Parent):
    def __init__(self):
        Parent.__init__(self)

    def method(self):
        super(Child, self).method()

child = Child()

if __name__ == '__main__':
     print(plus(2, 2))
     print(minus(4, 2))
     print(mul(3, 3))
     print(delit(8,2))
     print(delit(8,2)- mul(3,3))
