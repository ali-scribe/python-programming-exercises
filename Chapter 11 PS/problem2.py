# This example shows how inheritance works in a class hierarchy.
# A Dog is a Pet, and a Pet is an Animal.
class Animals:
    # This base class is empty on purpose.
    # It just demonstrates the relationship between classes.
    pass

class Pets(Animals):
    # Pets inherits all behavior from Animals.
    pass

class Dog(Pets):
    # A static method belongs to the class, not to a specific object.
    # It does not need self because it does not use object attributes.
    @staticmethod
    def bark():
        print("Woof! Woof!")

# Create an instance of Dog.
d = Dog()

# Call the bark method through the object.
d.bark()

# We could also call it directly from the class.
Dog.bark()

# Both versions work because bark() is static and does not depend on instance data.