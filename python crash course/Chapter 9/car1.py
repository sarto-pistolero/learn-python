from car import Car

car_1 = Car("Saab","9000","2001","Red")
print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.colour)

car_1.drive()

car_2 = Car("Volvo","XC90","2025","Black")
print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.colour)

car_2.drive()
print("At the redlight")
car_2.stop()