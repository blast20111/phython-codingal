class india():
    def Language(self):
        print("india language is hindi")
    def Capital(self):
        print("india capital is delhi")
    def type(self):
        print("india is a developing country")
class USA():
    def Language(self):
        print("USA language is english")
    def Capital(self):
        print("USA capital is new york")
    def type(self):
        print("USA is a developed country")
obji=india()
obju=USA()
for country in (obji,obju):
    country.type()
    country.Language()
    country.Capital()
