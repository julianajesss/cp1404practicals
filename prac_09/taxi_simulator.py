from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"

current_taxi = None
bill_to_date = 0
taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

print("Let's drive!")
print(MENU)
menu_choice = input(">>> ").lower()
while menu_choice != "q":
    if menu_choice == "c":
        print("Taxis available:")
        taxi_count = -1
        for taxi in taxis:
            taxi_count += 1
            print(f"{taxi_count} - {taxi}")
        taxi_choice = int(input("Choose taxi: "))
        if taxi_choice <= taxi_count:
            current_taxi = taxi_choice
        else:
            print("Invalid taxi choice")
    elif menu_choice == "d":
        if current_taxi is None:
            print("You need to choose a taxi before you can drive")
        else:
            distance_to_drive = int(input("Drive how far? "))
            taxis[current_taxi].drive(distance_to_drive)
            fare = taxis[current_taxi].get_fare()
            print(f"Your {taxis[current_taxi].name} trip cost you ${fare:.2f}")
            bill_to_date += fare
    else:
        print("Invalid option")
    print(f"Bill to date: {bill_to_date:.2f}")
    print(MENU)
    menu_choice = input(">>> ").lower()
print(f"Total trip cost: ${bill_to_date:.2f}")
print("Taxis are now:")
taxi_count = -1
for taxi in taxis:
    taxi_count += 1
    print(f"{taxi_count} - {taxi}")