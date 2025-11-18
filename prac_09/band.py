from prac_09.musician import Musician

class Band:
    """Depicts a band of Musicians."""

    def __init__(self, name):
        """Construct a band with a name and empty musicians list."""
        self.name = name
        self.musicians = []

    def __str__(self):
        return f"{self.name} ({self.musicians})"

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing each musician playing their first (or no) instrument."""
        for musician in self.musicians:
            Musician(musician).play()
