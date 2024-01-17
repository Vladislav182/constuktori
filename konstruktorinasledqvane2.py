class Animal:
    def __int__(self, name, age):
        self.name = name
        self.age = age

    def eat(self) :
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} is barking")


class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} is meowing")


dog = Dog('doggy', 5)
cat = Cat('Wiskas', 3)

dog.eat()
cat.eat()
dog.make_sound()
cat.make_sound()
