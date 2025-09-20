medical_cause= input("did you had your attendence y or n")
attendence=int(input("enter your attendence"))
if medical_cause=="y":
        print("you are allowed")
else:
        if attendence>=75:
                print("you are allowed")
        else:
                print("you are not allowed")

