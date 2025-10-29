"""
Estimate: 20min
Actual: 18min
"""


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        """Represent a guitar.

        name: string, model of guitar
        year: integer, year guitar was made
        cost: float, cost of guitar
        """

        self.name = name
        self.year = year
        self.cost = float(cost)

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        return 2025 - self.year

    def is_vintage(self):
        if self.get_age() >= 50:
            return True
        return False


def main():
    print("My guitars!")
    guitars = []
    guitars_count = -1
    longest_name = 0
    longest_cost = 0
    name = input("Name: ")
    while name != "":
        if len(name) > longest_name:
            longest_name = len(name)
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        cost_but_string = str(cost)
        if len(cost_but_string) > longest_cost:
            longest_cost = len(cost_but_string)
        guitars.append(Guitar(name, year, cost))
        guitars_count += 1
        print(f"{guitars[guitars_count]} added.")
        name = input("Name: ")
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        if guitar.is_vintage():
            vintage_string = "(vintage)"
        else:
            vintage_string = ""
        print(f"Guitar {i}: {guitar.name:>{longest_name}} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")


main()
