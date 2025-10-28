class ProgrammingLanguage:
    """Hold data on programing language."""

    def __init__(self, name="", typing="Static", reflection=True, year=0):
        """Initialise a ProgrammingLanguage instance.

        name: string, name of programing language
        typing: string, either Static or Dynamic
        reflection: boolean,
        year: integer, year of language creation
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"


    def is_dynamic(self):
        return self.typing == "Dynamic"