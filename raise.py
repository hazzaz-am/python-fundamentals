dict = {"A": "163", "B": "56 Au"}


def main():
    letter = input("Enter letter: ")
    try:
        au = float(dict[letter])
        m = au * 10
    except ValueError:
        print("No Value")
    else:
        print(m)

    get_min(20, 10)


def get_min(mile=10, min=0):
    if not min > 0:
        raise ValueError("Must be greater than 0")
    else:
        print(mile, min)


# main function call
main()
