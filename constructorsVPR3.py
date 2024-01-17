class MyClass:
    def __int__(self, name):
        self.name = name
    def __del__(self):
        print(f"Obektyt {self.name} se deleteva")
obj = MyClass('Primer')
print("Deistvie")