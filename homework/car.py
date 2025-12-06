class porsche():
    def Price  (self):
        print("Expensive, focused on luxury, comfort, and power mixed together")
    def Engine (self):
        print("More engine options (including V6, V8, hybrid), heavier but extremely powerful and refined.")
    def type(self):
        print("4-door luxury sport sedan, bigger and more comfortable for passengers.")
class toyota():
    def Price (self):
        print("Much cheaper, focused on fun driving and drifting vibes.")
    def Engine  (self):
        print("Smaller, lightweight, very responsive—feels like a classic JDM performance car.")
    def type(self):
        print("2-door sports car made for sharp handling and fast acceleration.")
obji=porsche()
obju=toyota()
for country in (obji,obju):
    country.type()
    country.Engine ()
    country.Price ()
