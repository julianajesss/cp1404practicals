"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    print(determine_grade(score))
    random_score = random.randint(0, 100)
    print(f"Random score: {random_score}\n{determine_grade(random_score)}")

def determine_grade(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    return "Bad"

main()
