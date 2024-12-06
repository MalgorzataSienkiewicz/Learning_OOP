class Human:
    def __init__(self, name, language):
        self.name = name
        self.language = language

    def speak(self):
        if self.language == 'pl':
            print(f"Czesc, mam na imie {self.name}")
        elif self.language == 'en':
            print(f'Hi, my name is {self.name}')

class Dog:
    def __init__(self, language):
        self.language = language

    def bark(self):
        if self.language == 'pl':
            print('Hau! Hau!')
        elif self.language == 'en':
            print('Woof! Woof!')

class Mutant(Human, Dog):
    def __init__(self, name, language):
        Human.__init__(self, name, language)
        Dog.__init__(self, language)

mutant = Mutant('Dogmeat', 'pl')
mutant.speak()
mutant.bark()
