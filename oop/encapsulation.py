import datetime


class Vehicle:
    def __init__(self, brand, year):
        self.__brand = brand
        self.__year = year

    @property
    def brand(self):
        return self.__brand

    @property
    def year(self):
        return self.__year

    @brand.setter
    def brand(self, brand):
        if brand in ["Tesla", "Toyota", "BMW", "Honda"]:
            self.__brand = brand
        else:
            print("This brand is not allowed")

    @year.setter
    def year(self, year):
        currentYear = datetime.datetime.now().year
        if year < currentYear:
            self.__year = year
        else:
            print("Year: cannot be in the future")


class Car(Vehicle):
    def __init__(self, brand, year, speed):
        super().__init__(brand, year)
        self.__speed = speed

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        if 0 <= speed <= 200:
            self.__speed = speed
        else:
            print("Cannot accelerate more than 200")

    @Vehicle.brand.setter
    def brand(self, brand):
        print("Car brand check...")
        return super(Car, type(self)).brand.__set__(self, brand)


class ElectricCar(Car):
    def __init__(self, brand, year, speed, battery):
        super().__init__(brand, year, speed)
        self.__battery = battery

    @property
    def battery(self):
        return self.__battery

    @battery.setter
    def battery(self, battery):
        if 0 <= battery <= 100:
            self.__battery = battery
        else:
            print("Battery cannot be more than 100")

    @Car.speed.setter
    def speed(self, speed):
        if speed > 150:
            print("Cannot exceed 150")
        else:
            super(ElectricCar, ElectricCar).speed.__set__(self, speed)

    @Car.brand.setter
    def brand(self, brand):
        if brand in ["Tesla", "BMW"]:
            super(ElectricCar, ElectricCar).brand.__set__(self, brand)
        else:
            print("Brand must be Tesla or BMW")


class Vehicle:
    def __init__(self, brand, year):
        self.__brand = brand
        self.__year = year

    def get_brand(self):
        return self.__brand

    def get_year(self):
        return self.__year

    def set_brand(self, brand):
        if brand in ["Tesla", "Toyota", "BMW", "Honda"]:
            self.__brand = brand
        else:
            print("This brand is not allowed")

    def set_year(self, year):
        currentYear = datetime.datetime.now().year
        if year < currentYear:
            self.__year = year
        else:
            print("Year: cannot be in the future")


class Car(Vehicle):
    def __init__(self, brand, year, speed):
        super().__init__(brand, year)
        self.__speed = speed

    def get_speed(self):
        return self.__speed

    def set_speed(self, speed):
        if 0 <= speed <= 200:
            self.__speed = speed
        else:
            print("Cannot accelerate more than 200")

    def set_brand(self, brand):
        print("Car brand check...")
        return super().set_brand(brand)


class ElectricCar(Car):
    def __init__(self, brand, year, speed, battery):
        super().__init__(brand, year, speed)
        self.__battery = battery

    def get_battery(self):
        return self.__battery

    def set_battery(self, battery):
        if 0 <= battery <= 100:
            self.__battery = battery
        else:
            print("Battery cannot be more than 100")

    def set_speed(self, speed):
        if speed > 150:
            print("Cannot exceed 150")
        else:
            super().set_speed(speed)  # call Car's setter

    def set_brand(self, brand):
        if brand in ["Tesla", "BMW"]:
            super().set_brand(brand)  # call Vehicle via Car
        else:
            print("Brand must be Tesla or BMW")


class Vehicle:
    def __init__(self, brand):
        self.__brand = brand

    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        if brand.lower() in ["tesla", "toyota", "bmw"]:
            self.__brand = brand
        else:
            print("Invalid brand!")


class Car(Vehicle):
    def __init__(self, brand, speed=0):
        super().__init__(brand)
        self.speed = speed

    def get_speed(self):
        return self.speed

    def set_speed(self, speed):
        if 0 <= self.speed <= 200:
            self.speed = speed
        else:
            print("🚫 Invalid speed!")

    def set_brand(self, brand):
        return super().set_brand(brand)


class ElectricCar(Car):
    def __init__(self, brand, speed, battery):
        super().__init__(brand, speed)
        self.__battery = battery

    def get_battery(self):
        return self.__battery

    def set_battery(self, battery):
        if 0 <= battery <= 100:
            self.__battery = battery
        else:
            print("🚫 Invalid battery level!")

    def set_speed(self, speed):
        if speed > 150:
            print("🚫 Electric car speed cannot exceed 150!")
        else:
            super().set_speed(speed)


tesla = ElectricCar("Tesla", 0, 100)

print(tesla.get_brand())  # Tesla
tesla.set_brand("Ferrari")  # 🚫 Invalid brand!
tesla.set_brand("BMW")  # ✅ allowed
print(tesla.get_brand())  # BMW

tesla.set_speed(160)  # 🚫 Electric car speed cannot exceed 150!
tesla.set_speed(140)  # ✅ allowed
print(tesla.get_speed())  # 140

tesla.set_battery(110)  # 🚫 Invalid battery level!
tesla.set_battery(90)  # ✅ allowed
print(tesla.get_battery())  # 90


class Car:
    def __init__(self, brand):
        self.__brand = brand


my_car = Car("Toyota")
print(my_car._Car__brand)
