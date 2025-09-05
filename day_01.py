name = input("What's your name? ")
# remove white spaces from strip start and ends
name = name.strip()

# capitalize string
name = name.capitalize()

# title case for string
name = name.title()
print("Hello,", name)

num1 = int(input("Enter first number 1: "))
num2 = int(input("Enter first number 2: "))

print(num1 + num2)

num3 = float(input("Enter first number 3: "))
num4 = float(input("Enter first number 4: "))

z = num3**num4
print(f"{z:.2f}")


def main(): 
  hello("Hazzaz")
  print(multiply(3))
  

def hello(name):
  print("Hello", name)


def multiply(n): 
  return n * n


main()