import random

number_of_quick_picks = int(input("How many quick picks? "))
for i in range(number_of_quick_picks):
    numbers = []
    for j in range(6):
        number = random.randint(1, 45)
        while number in numbers:
            number = random.randint(1, 45)
        numbers.append(number)
    numbers.sort()
    for number in numbers:
        print(f"{number:2}", end=" ")
    print()