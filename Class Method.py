print("Class Method")

# Change the class Attribute Salary @classmethod
class Employee:
    company = "Viva soft"
    salary = 100
    location = 'Dhaka'

    # change The class Attribute
    # def changeSalary(self,sal):
    #     self.__class__.salary = sal

    # change The class Attribute
    @classmethod
    def changeSalary(cls, sal): 
        cls.salary = sal


e = Employee()
print(e.salary)

e.changeSalary(300)
print(e.salary)

print(Employee.salary)


