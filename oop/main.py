class Person:
	
	def __init__(self, name, age, gender, designation):
		self.name = name
		self.age = age
		self.gender = gender
		self.designation = designation
		
	def getPersonInformation(self):
		return f"{self.name} is {self.age} years old and work as a {self.designation}."

p1 = Person("Hazzaz", 24, "Male", "Software Engineer")


class Parent:
	def __init__(self, childName):
		self.childName = childName
	

class Child(Parent):
	pass

child1 = Child("Hazzaz")
child2 = Child("Amin")


class Factory:
	def __init__(self, materials):
		self.materials = materials

class DhakaFactory(Factory):
	def __init__(self, materials, colors):
		super().__init__(materials)
		self.colors = colors

class ChittagongFactory(DhakaFactory):
	def __init__(self, materials, colors, zips):
		super().__init__(materials, colors)
		self.zips = zips
	
	def getChittagongInformation(self):
		return f"{self.materials} {self.colors} {self.zips}"


fc = ChittagongFactory("Cloth", "Black", 2)

