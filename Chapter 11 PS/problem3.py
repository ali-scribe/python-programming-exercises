class Employee:
    # These are class attributes: shared values for all Employee objects.
    salary = 234
    increment = 20

    # A property lets us access a computed value as if it were a normal attribute.
    @property
    def salaryAfterIncrement(self):
        # salary + percentage increase
        return self.salary + (self.salary * self.increment / 100)

    # This sets the value whenever we assign to salaryAfterIncrement.
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, new_salary):
        # Formula for percent increase:
        # new_salary = old_salary * (1 + increase_percent/100)
        # So increase_percent = (new_salary / old_salary - 1) * 100
        self.increment = ((new_salary / self.salary) - 1) * 100

# Create one Employee object.
e = Employee()

# Assign a new salary value.
# Because salaryAfterIncrement is a property, the setter runs automatically.
e.salaryAfterIncrement = 280.8

# The salary increased from 234 to 280.8.
# That is a 20% increase, so increment should be 20.0.
print(round(e.increment, 2))