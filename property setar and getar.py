print("Property : ")

class Employee:
    company = 'viva Soft'
    salary = 5600
    salaryBonus = 400

    @property
    def totalSalary(self):
        return self.salary+self.salaryBonus

    # setter method
    @totalSalary.setter
    def totalSalary(self, value):
        self.salaryBonus = value - self.salary




e=Employee()
print(e.totalSalary)
e.totalSalary = 5800
print(e.salary)
print(e.salaryBonus)
