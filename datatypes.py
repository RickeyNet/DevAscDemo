from classes.my_classes import Car

my_car = Car(make="Jeep", model="wagoneer", year=2024, mileage=3000, color="Nordic Grey", condition="New")

my_wifes_car = Car(make="Toyota", model="Camry", year=2020, mileage=15000, color="Blue", condition="Used")

print(my_wifes_car.__dict__)
