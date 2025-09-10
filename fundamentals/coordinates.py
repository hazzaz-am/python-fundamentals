import sys


def main():
    coordinates = (2323.232, -34343.344)
    coordinates_list = [2323.232, -34343.344]
    print(coordinates[0])
    print(len(coordinates))
    print(sys.getsizeof(coordinates))
    print(sys.getsizeof(coordinates_list))


main()
