a = 100
b = 335
c = 300
weekday = "Jumabar"


month = 5
day = 4
match day:
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("A weekday in April")
    case 1 | 2 | 3 | 4 | 5 if month == 5:
        print("A weekday in May")
    case _:
        print("No match")


match weekday:
    case 0:
        print("Saturday")
    case 1 | "break":
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6 | "Jumabar":
        print("Friday")
    case _:
        print("No week day")

if a > b:
    pass
else:
    print("b ig bigger")


if not a > b:
    print("a is not big")


if a > b or c > a:
    print("c is bigger")


if a > b and c > a:
    print(f"c is greater than {a}, {b}")


if 4 == 4:
    print("Not Equal")

print(2) if 2 > 7 else print(3)
print(a) if a > b else print("=") if b == a else print(b)
