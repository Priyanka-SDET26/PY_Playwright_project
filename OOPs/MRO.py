class A:
    x, y = 10, 20

    def m1(self):
        print(self.x + self.y)  # 10 + 20 = 30


class B:
    a, b = 2, 3

    def m1(self):
        print(self.a + self.b)  # 2 + 3 = 5

#❌ 'self' doesn't exist outside a method
class C(A, B):

    def call_methods(self):
        print("Calling A's m1:")
        A.m1(self)  # ✅ Pass self explicitly → accesses A's x, y

        print("Calling B's m1:")
        B.m1(self)  # ✅ Pass self explicitly → accesses B's a, b


# Create object of C
cObj = C()
cObj.call_methods()
# 1️⃣ Direct call — MRO decides (A wins)
cObj.m1()              # → 30  (A's method)

# 2️⃣ Unbound call — You decide
A.m1(cObj)             # → 30  (A's method)
B.m1(cObj)             # → 5   (B's method)

# 3️⃣ Inside child method using self
class C(A, B):
    def call_methods(self):
        A.m1(self)     # → 30  ✅
        B.m1(self)     # → 5   ✅


#Rule: Whenever a class, method, loop, or condition has no body,
# always write pass — it tells Python "I'm intentionally leaving this empty!"