from abc import ABC,abstractmethod
class animal(ABC):
    def move(self):
        pass
class human(animal):
    def move(self):
        print("i can walk an run")
class dog(animal):
    print("i can bark")
class cat(animal):
    print("i can meow")
class snake(animal):
    print("i can crawl")
a=human()
a.move()
b=dog()
b.move()
c=cat()
c.move()
d=snake()
d.move()

