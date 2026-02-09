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