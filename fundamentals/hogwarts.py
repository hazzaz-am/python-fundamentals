# lists
students = ["Hazzaz", "Harry", "Hogwart"]

for i in range(len(students)):
    print(i)

for i in range(len(students)):
    print(students[i])

for student in students:
    print(student)

# Dictionaries
students = {"Hazzaz": "Dhaka", "Milan": "UK"}

print(students["Hazzaz"])

for name in students:
    print(name)

for live in students:
    print(students[live])


for student in students:
    print(student, students[student], sep=", ")

students = [
    {"name": "Hazzaz", "house": "Dhaka", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Slytherin", "patronus": None},
]


for student in students:
    print(
        student["name"],
        " lives in ",
        student["house"],
        " with his patronus ",
        student["patronus"],
    )
