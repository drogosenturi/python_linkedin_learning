##  CLASSES AND OBJECT
class Dog: #uppercase letter for class names
    #everything within indent defines the class
    def __init__(self, name): ## two underscores on either side for initialization
        self.name = name
        self.legs = 4

    def speak(self):
        print(self.name + ': Bark!')

my_dog = Dog('Rover') ## CLASS NOT A FUNCTION
another_dog = Dog('Fluffy')

my_dog.speak() ## refers to the speak part of the function
another_dog.speak()

