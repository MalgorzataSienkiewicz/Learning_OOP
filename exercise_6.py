from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(f"Name is {self.name}")

    @abstractmethod
    def calculate_salary(self):
        pass

class Developer(Employee):
    def __init__(self, name, base_salary):
        super().__init__(name)
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary

class Manager(Employee):
    _bonus = 1000

    def __init__(self, name, base_salary):
        super().__init__(name)
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary + self._bonus

employee = Developer("Gosia", 10000)
print(employee.calculate_salary())
employee1 = Manager("Tomek", 10000)
print(employee1.calculate_salary())