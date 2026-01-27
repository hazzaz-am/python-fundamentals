from pathlib import Path
import os

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

def readFile():
	readFileAndFolder()
	try:
		name = input("Which file do you want to read? : ")
		path = Path(name)
		if path.exists() and path.is_file():
			with open(path, "r") as fs:
				data = fs.read()
				print(data)
		else:
			print("File does not exist.")
	except Exception as error:
		print(f"Error occurred: {error}")
	
def updateFile():
	readFileAndFolder()
	try:
		name = input("Which file do you want to update? : ")
		path = Path(name)
		if path.exists() and path.is_file():
			print("Press 1 for rename this file.")
			print("Press 2 for add data to this file.")
			print("Press 3 for overwrite content for this file.")
			
			res = int(input("Enter your choice: "))
			
			if res == 1:
				p2_name = input("Enter new file name: ")
				path.rename(p2_name)
				print("File rename successfully completed.")
			if res == 2:
				with open(path, "a") as fs:
					data = input("What you want to add? ")
					fs.write(f"\n{data}")
					print("File updated successfully.")
			if res == 3:
				with open(path, "w") as fs:
					data = input("What content do you want to add after overwriting? ")
					fs.write(data)
					print("File overwritten completed successfully.")
		else:
			print("File does not exist.")
	except Exception as error:
		print(f"Error occurred: {error}")

def deleteFile():
	readFileAndFolder()
	try:
		name = input("Which file do you want to delete? : ")
		if os.path.exists(name):
			os.remove(name)
			print("File deleted successfully.")
		else:
			print("File does not exist.")
	except Exception as error:
		print(f"Error occurred: {error}")

print("Press 1 for creating a file.")
print("Press 2 for reading a file.")
print("Press 3 for updating a file.")
print("Press 4 for deleting a file.")

check = input("Enter your choice: ")
if check == "1":
	createFile()
elif check == "2":
	readFile()
elif check == "3":
	updateFile()
elif check == "4":
	deleteFile()