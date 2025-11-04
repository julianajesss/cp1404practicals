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

    def __lt__(self, other):
        return self.year < other.year

    def get_age(self):
        return 2025 - self.year

    def is_vintage(self):
        if self.get_age() >= 50:
            return True
        return False

