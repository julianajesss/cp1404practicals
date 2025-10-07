"""
3
2
1
3, 1, 4, 1, 5, 9, 2
1, 5
True
False
False
error?

3
2
1
[3, 1, 4, 1, 5, 9]
[1]
True
False
False
[3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
"""

numbers = [3, 1, 4, 1, 5, 9, 2]

print(numbers[0])
print(numbers[-1])
print(numbers[3])
print(numbers[:-1])
print(numbers[3:4])
print(5 in numbers)
print(7 in numbers)
print("3" in numbers)
print(numbers + [6, 5, 3])

numbers[0] = "ten"
numbers[-1] = 1
print(numbers)
print(numbers[1:-1])
print(9 in numbers)
