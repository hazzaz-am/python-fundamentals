class Dunder:
  def __init__(self, age):
    self.age = age

  def __str__(self):
    return f"Your age is {self.age}"
  
  def __add__(self, other):
    return f"Your age {self.age} and you brother's age {other.age} = {self.age + other.age}"
  
d = Dunder(24)
b = Dunder(18)
print(d + b)