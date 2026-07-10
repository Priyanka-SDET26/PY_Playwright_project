

class Employee :

    def __init__(self, Salary):
            self.__salary = Salary

#both method should be named with same name
    @property
    def salary(self):
           return self.__salary

    @salary.setter
    def salary (self, Salary):
        EmployeeID = input("Enter your EmployeeID :  ")

        if EmployeeID == "AI539" :
            self.__salary = Salary
        print("Congratulation! AI539 Priyanka , Your Salary is hiked to 1598205 now")


obj = Employee(120000)

obj.salary = 1598205 # propery setter  method should be called with assignment
print(obj.salary) # property method dont need () to call