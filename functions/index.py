def change_case(func):
    def inner_change(name):
        return func(name).upper()

    return inner_change


@change_case
def my_function(name):
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
