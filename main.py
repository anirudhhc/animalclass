# import necessary changes
from abc import ABC
class animal(ABC):

    def move(self):
        pass

class Human(animal):
    def move(self):
        print("i can run and walk")

class snake(animal):
    def move(self):
        print("i can crawl")

class dog(animal):
    def move(self):
        print("i can bark")

class lion(animal):
    def move(self):
        print("i can roar")

R=Human()
R.move()

K=snake()
K.move()

R= dog()
R.move()

R=lion()
R.move()


        

