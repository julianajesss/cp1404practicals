import random

from prac_09.car import Car

class UnreliableCar(Car):
    """Specialised version of a Car that includes a reliability level of if drive will work."""

    def __init__(self, name, fuel, reliability):
        """Initialise a UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car a given distance.

        If the reliability is lower than a randomly generated number between 1 and 100 then
        drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        """
        if random.randint(0, 100) > self.reliability:
            distance = 0
        else:
            if distance > self.fuel:
                distance = self.fuel
                self.fuel = 0
            else:
                self.fuel -= distance
            self._odometer += distance
        return distance
