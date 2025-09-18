import csv

name = input("What's your name: ")
names = []
students = []
name = input("What's your name: ")
house = input("Where you have been: ")


with open("students.csv", "a") as file:
    # writer = csv.writer(file)
    writer = csv.DictWriter(file, fieldnames=["name", "house"])
    writer.writerow({"name": name, "house": house})


with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "house": row["house"]})


for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student["name"]} is in {student["house"]}")


with open("students.csv") as file:
    reader = csv.reader(file)
    for name, house in reader:
        students.append({"name": name, "house": house})


for student in sorted(students, key=lambda student: student["name"], reverse=True):
    print(f"{student['name']} is in {student['house']}")


with open("students.csv") as file:
    reader = csv.reader(file)
    for name, house in reader:
        students.append({"name": name, "house": house})


for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")


with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)


for student in sorted(students, key=lambda student: student["house"], reverse=True):
    print(f"{student['name']} is in {student['house']}")


def get_name(student):
    return student["house"]


for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['house']}")


with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")


for student in sorted(students, reverse=True):
    print(student)


with open("students.csv") as file:
    for student in file:
        row = student.rstrip().split(",")
        print(f"{row[0]} lives in {row[1]}")


with open("names.txt", "r") as file:
    for name in file:
        names.append(name.strip())

for name in sorted(names):
    print(name)


with open("names.txt", "r") as file:
    for name in sorted(file):
        print(name.rstrip())


with open("names.txt", "r") as file:
    # names = file.readlines()
    for name in file:
        print(f"Hello, {name.rstrip()}")


with open("names.txt", "a") as file:
    file.write(f"{name}\n")

file = open("names.txt", "a")
file.write(f"{name}\n")
file = open("names.txt", "w")
file.close()
