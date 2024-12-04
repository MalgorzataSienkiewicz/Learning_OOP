class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def is_adult(self):
        return self.age >= 18
    
    def print_description(self):
        print(f"User is name {self.name} and is {self.age} years old.")

class InheritedUser(User):
    def __init__(self, name, age, last_name):
        super().__init__(name, age)
        self.last_name = last_name


user = InheritedUser('Kamil', 36, 'Krawczyk')
print(user.name)
print(user.age)
print(user.last_name)