class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"Kazvam se {self.name} na {self.age}")
class Student(Person):
    def __int__(self, name, age, grade):
        super().__init__(name, age,)
        self.grade = grade
    def study(self):
        print(f"{self.name} study hard")
    def introduce(self):
        super().introduce()
        print(f"I am in grade{self.grade}")
person = Person("John", 25)
person.introduce()
student = Student("Alice", 18)
student.introduce()
student.study()
