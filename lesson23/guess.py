import random
import time
num=random.randint(1,100)
def intro():
    print("may i ask for your name?")
    global name
    name=input()
    print (name+"we are going to play a game .I am going to think a number between 1 to 100")
    if num%2==0:
        x="even"
    else:
        x="odd"
    print("this is a "+x+"number")
    time.sleep(.5)
    print("go ahead,guess")
def pick():
    guessestaken=0
    while guessestaken<6:
        time.sleep(.25)
        enter=input("guess:")
        try:
            guess=int(enter)
            if guess<=100 and guess>=1:
                guessestaken+=1
                if guessestaken<6:
                    if guess<num:
                        print("the guess is too low")
                    if guess>num:
                        print("the guess is too high")
                    if guess!=num:
                        time.sleep(.5)
                        print("try again!")
                    if guess==num:
                        break
            if guess>100 or guess<1:
                print("the number is not in range")
                time.sleep(.25)
                print("enter a number between 1 and 100")
        except:
            print("i dont think"+enter+"is a number,sorry")
    if guess==num:
        print("good job!,"+guessestaken+"guess")
    if guess!=num:
        print("the number was"+str(num))
playagain="yes"
while playagain=="yes":
    intro()
    pick()
    print("do u want to play again")
    playagain=input()