import random
class fruitquiz:
    def __init__(self):
        self.fruits={'apple':'red',
                     'orange':'orange',
                     'mango':'yellow',
                     'guava':'green',
                     'blueberry':'blue'}
    def quiz(self):
        while(True):
            fruit,color=random.choice(list(self.fruits.items()))
            print("what is the color of",fruit)
            answer=input()
            if(answer.lower()==color):
                print("correct answer")
            else:
                print("wrong answer")
            option=int(input("enter 0 if you want to play otherwise enter 1:"))
            if(option):
                break
print("welcome to fruit quiz")
fq=fruitquiz()
fq.quiz()

