
class A:


    def m1(self, x=10, y=20):
        print(x+y)


class B:

    a,b =2,3

    def m1(self):
        print(self.a+self.b)


class C(A,B):
    B.m1(self)
   pass
c= C()

