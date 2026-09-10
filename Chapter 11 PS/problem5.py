# A vector is a mathematical object with components.
# This version stores x, y, and z values, so it can represent a 3D vector.
class Vector:
    # Constructor: runs when a new Vector object is created.
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # __add__ defines how two vectors are added together.
    # Example: (x1, y1, z1) + (x2, y2, z2) = (x1+x2, y1+y2, z1+z2)
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    # __mul__ defines scalar multiplication.
    # Example: 2 * (x, y, z) = (2x, 2y, 2z)
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)

    # __str__ controls how the object prints in the terminal.
    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

# Test the implementation.
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

# Add vectors: (1,2,3) + (4,5,6) = (5,7,9)
print(v1 + v2)

# Multiply a vector by a scalar: 2 * (1,2,3) = (2,4,6)
print(v1 * v2)
