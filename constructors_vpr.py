class Person:
    def __init__(self, name, l_name):
        self.name = name
        self.l_name = l_name
    def introduce(self):
        print(f"Kazvam se {self.name}{self.l_name}")

person = Person('Vladislav', 'Dimitrov')
print(person.name)
print(person.l_name)
