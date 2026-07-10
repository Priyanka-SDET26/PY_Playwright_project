
class Overload:

    def m1(self,*Vars):

        total =0
        for Var in Vars:
            total = total+Var
        return total


Overload_obj = Overload()
print(Overload_obj.m1(1,2,3,4,5))