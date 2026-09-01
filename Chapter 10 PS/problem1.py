class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin



p = Programmer("John", 1200000 , 203302)
print(p.name, p.salary, p.pin, p.company)


p = Programmer("Rohan", 70000 , 28739)
print(p.name, p.salary, p.pin, p.company)