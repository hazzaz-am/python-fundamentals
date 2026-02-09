def decorate(func):
  def wrapper(a, b):
    print("I am before the function call")
    func(a, b)
    print("I am after the function call")
  return wrapper

@decorate
def addition(a, b):
  print(a + b)

def sum(*args):
  sum = 0
  for i in args:
    sum += i
  return sum

def information(**kwargs):
  print(kwargs)

def subtraction_decorator(func):
  def wrapper(*args, **kwargs):
    print("Before Function Call")
    func(*args, **kwargs)
    print("After Function Call")
  return wrapper

@subtraction_decorator
def sub(a, b, c):
  print(a - b * c)

sub(c = 1, a = 2, b = 3)
sub(1, 2, 3)
