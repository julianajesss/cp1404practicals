for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c
number_of_stars = int(input("Stars: "))
for i in range(1, number_of_stars + 1):
    print("*", end=" ")
print()

# d
number_of_stars = int(input("Stars: "))
current_stars = 1
while current_stars != number_of_stars:
    for i in range(1, current_stars +1):
        print("*", end=" ")
        print()
    current_stars += 1
for i in range(1, number_of_stars + 1):
    print("*", end=" ")
print()