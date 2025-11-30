class myClass:
    __privateVar=27
    def __privMeth(self):
        print("im inside class myclass")
    def hello(self):
        print("private variable value:",myClass.__privateVar)
foo=myClass()

foo.__privateVar=28
foo.hello()