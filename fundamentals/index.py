a = str(4)
b = int(3)

x, y, z = "Third Last", "Second Last", "Last"

name = friend_name = son_name = "Hazzaz"

# print(type(a))
# print(type(b))
# print(x, y, z)
# print(type(x), type(y), type(z))

# print(name, friend_name, son_name)

global_var = "Python is awesome"


def main():
    global var
    global global_var
    var = "Global variable"
    global_var = "Python is interesting"
    # print(global_var)


def global_variable():
    print(global_var)


main()
global_variable()
# print(global_var)
# print(var)
