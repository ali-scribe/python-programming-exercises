# Inheritance means a class can reuse code from another class.
# Here, a 2D vector is the base class, and a 3D vector extends it.
class TwoDVector:
    # __init__ is a constructor. It runs when a new object is created.
    def __init__(self, i, j):
        # These are instance variables; each object stores its own values.
        self.i = i
        self.j = j

    # A method describes behavior of the object.
    def show(self):
        # Display the vector using i and j notation.
        print(f"The vector is: {self.i}i + {self.j}j")

# A 3D vector inherits from 2D vector, so it gets i and j automatically.
# It adds a third component, k.
class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        # super() calls the parent class constructor to initialize i and j.
        super().__init__(i, j)
        self.k = k

    # This method overrides the parent method, so 3D vectors print differently.
    def show(self):
        print(f"The vector is: {self.i}i + {self.j}j + {self.k}k")

# Create a 2D vector object.
a = TwoDVector(1, 2)
a.show()

# Create a 3D vector object.
b = ThreeDVector(5, 2, 3)
b.show()