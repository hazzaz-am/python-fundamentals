from pathlib import Path


def readFileAndFolder():
	path = Path("")
	items = list(path.rglob("*"))
	for i, item in enumerate(items):
		print(f"{i + 1}. {item}")


def createFile():
	readFileAndFolder()
	try:
		name = input("Enter file name: ")
		path = Path(name)
		if not path.exists():
			with open(name, "w") as fs:
				data = input("What you want to write? ")
				fs.write(data)
			print("File created successfully.")
		else:
			print(f"{name} already exists.")
	except Exception as error:
		print(f"Error occurred: {error}")

def updateFile():
	pass

print("Press 1 for creating a file.")
print("Press 2 for updating a file.")
print("Press 3 for deleting a file.")
print("Press 4 for updating a file.")

check = input("Enter your choice: ")
if check == "1":
	createFile()