
from abc import ABC, abstractmethod

class abstract(ABC):

    @abstractmethod
    def method1(self):
        pass
    @staticmethod
    def method2(var):
        print(f"var is : {var}")
#obj = abstract()

class implement(abstract):

    def method1(self):
        print("congrstulations! Priyanks you got 40 % salary hike this year")

obj = implement()
obj.method1()
abstract.method2("15.6lacks")