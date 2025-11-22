class pt:
    species="dog"
    def __init__(self,breed,age):
        self.name=breed
        self.age=age
blu=("energetic dog breed",5)
woo=("working sled dog",10)
print("blu is"+blu.species+"species")
print("woo is"+blu.species+"species")
print("blu name is"+blu.breed+"and blu age is",blu.age)
print("woo name is"+woo.breed+"and blu age is",woo.age)

