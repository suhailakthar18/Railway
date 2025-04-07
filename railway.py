import random

class Railway:
    def __init__(self, trainNO, departure_time, source, destination):
        self.trainNO = trainNO
        self.departure_time = departure_time
        self.source = source
        self.destination = destination

    def book(self):
        return f"Ticket Booked from {self.source} to {self.destination} for train {self.trainNO} at {self.departure_time}"

    def status(self):
        return f"Train {self.trainNO} is running on time"

    def fare(self):
        return f"Fare for train {self.trainNO} is ₹{random.randint(100, 500)}"
