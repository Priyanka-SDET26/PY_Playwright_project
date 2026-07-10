class A:
    var1 = 1
    def m1(self):
       print("this is m1 from class A")


class B(A):
    var1 = 2
    def m1(self, x):
        print("This is m1 from class B")
        print(self.var1)


obj_B = B()

super(B, obj_B).m1()
obj_B.m1(10)
A.m1(B)
