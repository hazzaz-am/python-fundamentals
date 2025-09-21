class A:
    def test(self):
        return "A"


class B(A):
    def test(self):
        return super().test() + " B"


class C(A):
    def test(self):
        return super().test() + " C"


class D(B, C):
    def test(self):
        return super().test() + " D"


print(D.__mro__)


class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        return "Starting engine"


class Car(Vehicle):
    def __init__(self, brand, speed=0):
        super().__init__(brand)
        self.speed = speed

    def start(self):
        return super().start() + " Ready to drive"


class ElectricCar(Car):
    def __init__(self, brand, speed, battery):
        super().__init__(brand, speed)
        self.battery = battery

    def start(self):
        return super().start() + " Silent electric start"


tesla = ElectricCar("Tesla", 0, 100)

print(tesla.brand)  # Tesla
print(tesla.speed)  # 0
print(tesla.battery)  # 100

print(tesla.start())
print(ElectricCar.__mro__)
# Starting engine + Ready to drive + Silent electric start


class Car:
    def __init__(self, brand, speed=0):
        self.brand = brand
        self.speed = speed

    def accelerate(self):
        self.speed += 1
        return self.speed

    def brake(self):
        self.speed = max(0, self.speed - 1)
        return self.speed


class RacingCar(Car):
    def turbo(self):
        self.speed += 10
        return self.speed


ferrari = RacingCar("Ferrari", 50)

print(ferrari.brand)  # inherited attribute → Ferrari
print(ferrari.speed)  # 50
print(ferrari.accelerate())  # inherited method → 51
print(ferrari.turbo())  # new method in RaceCar → 61


class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def accelerate(self):
        self.speed += 1
        return self.speed

    def brake(self):
        self.speed -= 1
        return self.speed


my_car = Car("Tesla", 5)
print(my_car.accelerate())  # ?
print(my_car.accelerate())  # ?
print(my_car.brake())  # ?
print(my_car.speed)  # ?


class Hero:
    heroes_created = 0

    def __init__(self, name):
        self.name = name
        Hero.heroes_created += 1

    @classmethod
    def how_many_heroes(cls):
        print(f"Total heroes created: {cls.heroes_created}")


ironman = Hero("IronMan")
thor = Hero("Thor")

Hero.how_many_heroes()


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)


for x in myiter:
    print(x)

my_tuple = ("apple", "banana", "cherry")
myit = iter(my_tuple)

print(next(myit))
print(next(myit))
print(next(myit))


mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))


class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, firstname, lastname, year):
        super().__init__(firstname, lastname)
        self.graduationyear = year

    def welcome(self):
        print(
            "Welcome",
            self.firstname,
            self.lastname,
            "to the class of",
            self.graduationyear,
        )


x = Student("Mike", "Olsen")
x.printname()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def my_func(self):
        print("Hello, I am " + self.name)

    def __str__(self):
        return f"{self.name} is {self.age}"


p1 = Person("Hazzaz", 24)
p1.my_func()
p1.age = 25
del p1
print(p1)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age}"


p1 = Person("Hazzaz", 24)
print(p1)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("Hazzaz", 24)
print(p1.name)
print(p1.age)


class MyClass:
    x = 5


p1 = MyClass()
print(p1.x)
