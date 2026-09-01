# Import random so the fare can be generated with a random value.
from random import randint

# This class represents a train and stores its train number.
class Train:

    # Constructor: initializes the train number when a Train object is created.
    def __init__(self, trainNO):
        self.trainNO = trainNO

    # Book a ticket from one place to another.
    def book(self, fro, to):
        print(f"Your ticket is booked from {fro} to {to} on train number {self.trainNO}.")

    # Show the current status of the train.
    def getStatus(self):
        print(f"Train number {self.trainNO} is on time.")

    # Generate a random fare for the route.
    def getFare(self, fro, to):
        print(f"Ticket fare in train no. {self.trainNO} from {fro} to {to} is Rs. {randint(222, 500)}.")


# Create a Train object with train number 12345.
t = Train(12345)

# Test the methods by booking a ticket and showing status and fare.
t.book("Delhi", "Mumbai")
t.getStatus()
t.getFare("Delhi", "Mumbai")