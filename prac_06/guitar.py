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
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : {self.cost:.2}"

    def get_age(self):
        return 2025 - self.year

    def is_vintage(self):
        if self.get_age() >= 50:
            return True
        return False
