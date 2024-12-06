
class InvalidAgeError(Exception):
    def __init__(self, message, error_code):
        super().__init__(message)
        self.error_code = error_code

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age >= 0:
            self._age = age
        else:
            raise InvalidAgeError(f"Name must be positive. Your value is {age}.", 3)

user = User('Gosia', -34)
print(user.name)
