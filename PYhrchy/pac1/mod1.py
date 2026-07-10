class Employee:

    def __init__(self, EID, ENAME, Salary):
        self.EID = EID
        self.ENAME = ENAME
        self.Salary = Salary

    def Details(self):
        print(f"EID : {self.EID}, ENAME :{self.ENAME}, Salary :{self.Salary}")