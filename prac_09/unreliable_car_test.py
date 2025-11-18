from prac_09.unreliable_car import UnreliableCar

bad_car = UnreliableCar("bad car", 180, 1)
bad_car.drive(30)
print(f"Car has fuel: {bad_car.fuel}")
print(bad_car)

good_car = UnreliableCar("good car", 180, 100)
good_car.drive(30)
print(f"Car has fuel: {good_car.fuel}")
print(good_car)