import sys


for argv in sys.argv[1:]:
    print(argv)


if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print(sys.argv[1])
