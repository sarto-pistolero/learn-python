car = 'subaru'
print("Is car == 'subaru'? I predict True")
print(car == 'subaru')

print("\nIs car == volvo? I predict False")
print(car == 'audi')

car = 'volvo'
print("Is car == audi? I predict False")
print(car == 'audi')

print("\nIs car == volvo? I predict True")
print(car == 'volvo')

cars = ['audi', 'bmw', 'subaru', 'toyota', 'honda']
for car in cars:
    if car != 'volvo':
        print(car.upper())
    else:
        print(car.title())     

