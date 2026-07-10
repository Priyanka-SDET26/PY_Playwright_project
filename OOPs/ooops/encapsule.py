
class Employee :

    def __init__(self, Salary):
            self.__salary = Salary


    def get_salary(self):
           return self.__salary


    def set_salary (self, Salary):
        EmployeeID = input("Enter your EmployeeID :  ")

        if EmployeeID == "AI539" :
            self.__salary = Salary
        print("Congratulation! AI539 Priyanka , Your Salary is hiked to 1598205 now")


obj = Employee(120000)

obj.set_salary(1598205)
print(obj.get_salary())