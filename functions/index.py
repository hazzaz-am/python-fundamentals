x = lambda a, b, c: a + b + c
print(x(3, 4, 5))


def decorator1(func):
    def wrapper(*args, **kwargs):
        print("Decorator 1: Before function call")
        result = func(*args, **kwargs)
        print("Decorator 1: After function call")
        return result

    return wrapper


def decorator2(func):
    def wrapper(*args, **kwargs):
        print("Decorator 2: Before function call")
        result = func(*args, **kwargs)
        print("Decorator 2: After function call")
        return result

    return wrapper


@decorator1
@decorator2
def add(a, b):
    return a + b


result = add(2, 3)
print("Result", result)


def change_case(func):
    def my_inner():
        return func().upper()

    return my_inner


def add_greeting(func):
    def my_inner():
        return "Hello, " + func() + " Have a good day!"

    return my_inner


@change_case
@add_greeting
def my_function():
    return "Tobias"


print(my_function())


def change_case(n):
    def change_case(func):
        def my_inner(*args, **kwargs):
            if n == 1:
                a = func(*args, **kwargs).lower()
            else:
                a = func(*args, **kwargs).upper()
            return a

        return my_inner

    return change_case


@change_case(2)
def my_function(name):
    return "Hello, " + name


print(my_function("amin"))


def change_case(func):
    def my_inner(*args, **kwargs):
        return func(*args, **kwargs).upper()

    return my_inner


@change_case
def my_function(name):
    return "Hello, " + name


print(my_function("Hazzaz"))


def change_case(func):
    def inner_change(name):
        return func(name).upper()

    return inner_change


@change_case
def my_function(name: str):
    return f"hello, {name}"


@change_case
def another_func():
    return "Return hello"


print(my_function("Hazzaz"))
print(another_func())


def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("Recursion Example Results:")
tri_recursion(6)


def my_function(*kids):
    for kid in kids:
        print(kid)


my_function("Emil", "Tobias", "Linus")


def my_function(child3, child2, child1):
    print("The youngest child is " + child3)
    print("Than child", child2)
    print("Than child", child1)


my_function(child1="Emil", child2="Tobias", child3="Linus")

