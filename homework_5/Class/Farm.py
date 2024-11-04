class Farm:
    def __init__(self, name):
        self.name = name

    def allAnimal(self):
        return f"{self.name} lives in this farm."
    
class Cat(Farm):
    def job(self):
        return f"{self.name} just sleeps."
    
class Dog(Farm):
    def job(self):
        return f"{self.name} protects the farm."
    
class Cow(Farm):
    def job(self):
        return f"{self.name} gives milk."
    
class Donkey(Farm):
    def job(self):
        return f"{self.name} carries heavy things."
    

cat = Cat("Mike")
dog = Dog("Reks")
cow = Cow("Sig'ir")
donkey = Donkey("Eshshak")

print(f"{dog.allAnimal()} {dog.job()}")