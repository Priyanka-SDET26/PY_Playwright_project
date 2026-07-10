class Student:

    def __init__(self, Stu, SNAME, Sgrade):
        self.Stu = Stu
        self.SNAME = SNAME
        self.Sgrade = Sgrade

    def Details(self):
        print(f"EID : {self.Stu}, ENAME :{self.SNAME}, Salary :{self.Sgrade}")