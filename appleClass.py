# OOP practice

# define a new class
class Apple:
     colour = ''
     flavour = ''

pinklady = Apple()
pinklady.colour = 'pink'
pinklady.flavour = 'sour'

# define method in class
class Piglet:
     name = 'piglet'
     years = 0
     def speak(self):
          print('Oink! I\'m {}! Oink!'.format(self.name))
     def pig_years(self):
          return self.years * 18
     
hamlet = Piglet() # creating an instance
hamlet.name = 'Hamlet'
hamlet.speak()

piggy = Piglet()
piggy.years = 3
print(piggy.pig_years())

# Constructors and other Special Methods

class Apple:
     # define the constructor
     def __init__(self, colour, flavour): # this is a special method
          '''This is an example doctrine'''
          self.colour = colour
          self. flavour = flavour
     # special STR method
     def __str__(self):
          return 'This apple is {} and {}.'.format(self.colour, self.flavour)
     

pinklady = Apple('pink','sour')
print(pinklady.colour)
print(pinklady.flavour)
print(pinklady)
help(Apple)
          
     
