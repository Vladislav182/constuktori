class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self. year = year
        self.is_running = False
    def start(self):
        if self.is_running:
            print("Kolata veche e startirana")
        else:

            self.is_running = True
            print("Kolata e startirana")
    def stop(self):
        if not self.is_running:
            print("Kolata veche e sprqna")
        else:
            self.is_running = True
            print("Kolata e sprqna")
    def honk(self):
        if self.is_running:
            print("Beep beep!")
        else:
            print("Kolata trqbva da e startirana za da zvuchi klaksona")
obj = Car('BMW', 'e46', '2005')
obj.start()
obj.stop()
obj.honk()