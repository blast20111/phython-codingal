from abc import ABC,abstractmethod
class ABCclass(ABC):
    def print(self,x):
        print("passed value",x)
    @abstractmethod
    def task(self):
        print("we are in absclass task")
class test_class(ABCclass):
    def task(self):
        print("we are inside self task")
obj=test_class()
obj.task()
obj.print(100)

