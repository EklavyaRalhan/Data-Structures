from abc import ABC, abstractmethod

class animal(ABC):

    def move(self):
        pass


class human(animal):
    def move(self):
        print("I can run")

class snake(animal):
    def move(self):
        print("I can slither")

class monkey(animal):
    def move(self):
        print("I can swing")

h = human()
h.move()

s = snake()
s.move()

m = monkey()
m.move()