
class Animal:
  def show(self):
    print("Hello I am Hazzaz")

class Human(Animal):
  def  show(self):
    print("Hi I am Software Developer")

class Factory:
  a = "Dhaka"

  def factory_type(self):
    print("This is type of Garments")

class Greetings:
  __a = "Hello"

  def sayHello(self):
    print(f"{Greetings.__a}, I am Hazzaz")

class Personal:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    self.__job = "Software Developer"
  
  def showInformation(self):
    print(f"My name is {self.name}. I am {self.age} years old and working as a {self.__job}.")

from abc import ABC, abstractmethod

class AbstractClass(ABC):
  @abstractmethod
  def perimeter(self):
    pass
  
  @abstractmethod
  def area(self):
    pass

class Circle(AbstractClass):
  def __init__(self, radius):
    self.radius = radius

  def perimeter(self):
    pass

  def area(self):
    pass

circ = Circle(5)