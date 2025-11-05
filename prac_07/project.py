class Project:
    def __init__(self, name="", start_date="", priority=0, cost_estimate=0.0, completion=0):
        """Represents a project.
        name: string, name of the project
        start_date: string, date the project started
        priority: integer, the priority of the project
        cost_estimate: float, the estimated cost for the project
        completion: integer, the percentage completion of the project
        """

        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion = completion

    def __str__(self):
        """Return a string of project information."""
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: {self.cost_estimate}, completetion: {self.completion}%"

    def __lt__(self, other):
        """Return boolean for less than other object."""
        return self.priority < other.priority
