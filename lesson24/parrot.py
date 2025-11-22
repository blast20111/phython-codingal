class parrot:
    species="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
blu=parrot("BLU",10)
woo=parrot("WOO",15)
print("blu is"+blu.species+"species")
print("woo is"+blu.species+"species")
print("blu name is"+blu.name+"and blu age is",blu.age)
print("woo name is"+woo.name+"and blu age is",woo.age)
