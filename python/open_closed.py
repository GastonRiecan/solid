# Open Closed Principle
# it means that the class is open to extends and close to change

"""
WRONG
"""
class SuperHeroWrong:
    def __init__(self, name):
        self.name = name

    def fly(self) -> str:
        return f'{self.name} -> flying'
    
    def super_strength(self) -> str:
        return f'{self.name} -> super strength'
    

"""
BETTER
"""
# class SuperHero:
# create a new version without breaking OCP
class SuperHero:
    def __init__(self, name):
        self.name = name

    def super_strength(self) -> str:
        return f'{self.name} -> super strength'

#SOLUTION:
#Crear una clase abstracta para definir como debe estar compuesto un SuperHero
class SuperHero(ABC):
    def __init__(self, name):
        self.name = name
        
    @abstractmethod
    def activate_power(self) -> str:
        pass

#Crear una clase individual para cada SuperHero que herede de la clase abc
class Superman(SuperHero):
    def activate_power(self) -> str:
        return f'{self.name} -> flying and super strength'

class Hulk(SuperHero):
    def activate_power(self) -> str:
        return f'{self.name} -> super strength (SMASH!)'

class InvisibleWoman(SuperHero):
    def activate_power(self) -> str:
        return f'{self.name} -> invisibility'

# Instanciamos los héroes reales
superman = Superman('Superman')
hulk = Hulk('Hulk')
invisible_woman = InvisibleWoman('Invisible Woman')


        


# running process
superman = SuperHeroWrong('superman')
print(superman.fly())
print(superman.super_strength())

hulk = SuperHeroWrong('hulk')
print(hulk.super_strength())
### ???? fix it
print(hulk.fly())

 # what happen if I need to and invisible woman? how to add invisibility just for her?
