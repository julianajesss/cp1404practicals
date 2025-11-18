from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi (specialised version of car) that includes fanciness and flagfall."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.current_fare_distance = 0
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        return f"{super.__str__()}, {self.current_fare_distance}km on current fare, ${self.price_per_km:.2f}/km plus flagfall of ${self.flagfall:.2f}"

