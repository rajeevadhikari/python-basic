# Create a function describe_animal() that takes an object of any class and calls its sound() method.
#  Define classes Cat and Bird with their own implementations of the sound() method. Pass objects of both classes to describe_animal().

# class Cat:
#     def sound(self):
#         return "Meow"

# class Bird:
#     def sound(self):
#         return "Tweet"

# def animal(animal):
#     print(f"The animal says: {animal.sound()}")

# cat = Cat()
# bird = Bird()

# animal(cat)  
# animal(bird) 


''' Define a base class Shape with a method area().
Create two derived classes Circle and Rectangle that implement the area() method differently.
Instantiate objects of both classes and call their area() methods. '''


# import math

# class Shape:
#     def area(self):
#         raise NotImplementedError("Subclasses must implement the area() method")

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self,):
#         return math.pi * self.radius ** 2

# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

# circle = Circle(5)
# rectangle = Rectangle(4,8)

# print(f"Area of the circle: {circle.area():.2f}")  
# print(f"Area of the rectangle: {rectangle.area()}")


'''
Write a Python program to create a base class Animal with a method sound() that prints "Animals make sounds."
 Create a derived class Dog that overrides the sound() method to print "Dogs bark."

 '''
# class Animal:
#     def sound(self):
#         print("Animals make sounds.")

# class Dog(Animal):
#     def sound(self):
#         print("Dogs bark.")

# animal = Animal()
# dog = Dog()

# animal.sound()
# dog.sound()  

"""
Define a class Vehicle with attributes like brand and speed. 
Create a subclass Car that adds a new attribute fuel_type.
 Instantiate the Car class and print all the attributes
"""
# class Vehicle:
#     def __init__(self, brand, speed):
#         self.brand = brand
#         self.speed = speed

# class Car(Vehicle):
#     def __init__(self, brand, speed, fuel_type):
#         super().__init__(brand, speed)
#         self.fuel_type = fuel_type

# my_car = Car(brand="Toyota", speed=180, fuel_type="Petrol")

# print(f"Brand: {my_car.brand}")  
# print(f"Speed: {my_car.speed} km/h")
# print(f"Fuel Type: {my_car.fuel_type}")
