x = int(input("Enter x: "))
y = int(input("Enter y: "))

if x > y:
  print("x is greater than y")
elif y > x:
  print("y is greater than x")
else:
  print("Both equal")
  
if x != y:
  print("x is not equal y")

if x == 0 and y == 0:
  print("Both are zero")
  
def main():
  x = int(input("What's the x: "))
  
  if is_even(x):
    print("Even")
  else:
    print("Odd")
    
    
def is_even(n):
  if n % 2 == 0:
    return True  
  else:
    return False

name = input("Enter your name: ")

match name:
  case "Hazzaz" | "Amin":
    print("Brothers")
  case _:
    print("I don't know")


main()