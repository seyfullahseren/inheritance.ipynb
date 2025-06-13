# Base class
class Shape:
    def area(self):
        pass
    # Derived classes
class Circle(Shape):
    def area(self):
        return 3.14 * 5 * 5  # Assume radius = 5

class Square(Shape):
    def area(self):
        return 4 * 4  # Assume side = 4
    # Polymorphism in action
shapes = [Circle(), Square()]
for shape in shapes:
    print("Area:", shape.area())

    class EnglishGreeting:
    def greet(self):
        print("Hello")

class SpanishGreeting:
    def greet(self):
        print("Hola")

def greet_someone(greeter):
    greeter.greet()

greet_someone(EnglishGreeting())
greet_someone(SpanishGreeting())