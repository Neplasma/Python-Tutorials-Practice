# inheritance

class Fruit:
     def __init__(self, name, colour, flavour):
          self.name = name
          self.colour = colour
          self.flavour = flavour
     def __str__(self):
          return '{} is {} and {}.'.format(self.name.capitalize(), self.colour, self.flavour)
     

# Apple classes are inherited from the Fruit class
class Apple(Fruit):
     pass

class Grape(Fruit):
     pass

granny_smith = Apple('gRannY_sMith','green','tart')
carnelian = Grape('carnelIan', 'purple','sweet')
print(granny_smith)
print(carnelian)

class Animal:
     sound = ''
     def __init__(self, name):
          self.name = name
     def speak(self):
          print('{sound} I\'m {name}! {sound}'.format(name=self.name, sound=self.sound))

class Piglet(Animal):
     sound = 'Oink!'

hamlet = Piglet('Hamlet')
hamlet.speak()

class Cow(Animal):
     sound = 'Mooo!'

milky = Cow('Milky White')
milky.speak()

