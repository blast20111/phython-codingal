class point:
    def __init__(self,x=1,y=1):
        self.x=x
        self.y=y
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
p1=point(2,3)
print(p1.__str__())