"""  Object-Oriented Programming in Python  """


class Employee:
    #  salary = 89
    #  name = "Noman"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def getSalary(self):
        return self.salary

    def getName(self):
        print(self.name)


noman = Employee("Noman", 25000)
print(noman.name, "gets salary :", noman.salary)
noman.getName()  # access the getName function

harry = Employee("Harry", 416545)
print(harry.name, "and salary is", 77877)
