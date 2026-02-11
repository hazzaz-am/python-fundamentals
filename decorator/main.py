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

# comprehension

li = [i for i in range(10) if i % 2 == 0]
dic = {i: i**2 for i in range(1, 10) }


# lambda function
addition = lambda a : "even" if a % 2 == 0 else "odd" 

add_two = lambda a : a * 2

def add2 (x):
  return x * 2

def check_even(x):
  if x % 2 == 0:
    return True
  else:
    return False

check_odd = lambda a : True if a % 2 == 1 else False
a = [1, 2, 3, 4, 5]

ans = map(add2, a)
an = filter(check_odd, a)
print(list(an))