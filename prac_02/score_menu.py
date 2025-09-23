"""
display menu
get choice
while choice != <quit option>
    if choice == <first option>
        <do first task>
    else if choice == <second option>
        <do second task>
    ...
    else if choice == <n-th option>
        <do n-th task>
    else
        display invalid input error message
    display menu
    get choice
<do final thing, if needed>
"""
MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"

def main():
    score = get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(determine_grade(score))
        elif choice == "S":
            show_stars(score)
        else:
            print("Not a valid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("farewell")

def get_valid_score():
    score = int(input("Score: "))
    while score > 100 or score < 0:
        print("Invalid score")
        score = int(input("Score: "))
    return score

def show_stars(score):
    print("*"*score)

def determine_grade(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    return "Bad"

main()