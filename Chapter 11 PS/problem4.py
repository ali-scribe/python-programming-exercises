# This program creates a custom data type called Complex.
# A complex number has a real part and an imaginary part.
# Example: a + bi, where a is the real part and b is the imaginary coefficient.

class Complex:
    # The constructor runs when we create a new object.
    def __init__(self, r, i):
        self.r = r  # real part
        self.i = i  # imaginary part

    # __add__ defines how + works between two Complex objects.
    # (a + bi) + (c + di) = (a + c) + (b + d)i
    def __add__(self, c2):
        return Complex(self.r + c2.r, self.i + c2.i)

    # __mul__ defines how * works between two Complex objects.
    # (a + bi) * (c + di) = (ac - bd) + (ad + bc)i
    def __mul__(self, c2):
        return Complex(
            self.r * c2.r - self.i * c2.i,
            self.r * c2.i + self.i * c2.r
        )

    # __str__ defines how Python prints the object.
    def __str__(self):
        return f"{self.r} + {self.i}i"

# Create two complex numbers.
c1 = Complex(1, 2)  # 1 + 2i
c2 = Complex(3, 4)  # 3 + 4i

# Use the custom operator overloads.
print("Addition:", c1 + c2)      # expected: 4 + 6i
print("Multiplication:", c1 * c2) # expected: -5 + 10i