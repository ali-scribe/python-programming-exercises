# This class defines a simple calculator that can perform
# basic math operations on a stored number.
class Calculator:
    # The constructor stores the number that will be used
    # in the calculations.
    def __init__(self, n):
        self.n = n

    # This method calculates and prints the square of the number.
    def square(self):
        print(f"The square is {self.n*self.n}")

    # This method calculates and prints the cube of the number.
    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")

    # This method calculates and prints the square root of the number.
    def squareroot(self):
        print(f"The square root is {self.n**0.5}")

    @staticmethod
    def hello():
        print("Hello, I am a calculator.")


# Create an object with the value 4.
a = Calculator(4)

# Call each method to display the square, cube, and square root.
a.square()
a.cube()
a.squareroot()