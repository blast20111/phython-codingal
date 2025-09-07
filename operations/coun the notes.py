amount=int(input("please enter the amount"))
note1=amount//100
note2=(amount % 100)//50
note3=((amount % 100) % 50)//10
print("the no. of 100's are:",note1)
print("the no.of 50's are:",note2)
print("the no. of 10's are:",note3)