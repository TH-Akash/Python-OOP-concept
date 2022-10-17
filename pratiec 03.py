print("Employee,Add salary,Increment,Decrement")

class Employee:
    company = "Viva soft"
    salary = 3500
    increment = 1.5

    @property
    def salaryAfterIncrement(self):
        return self.salary * self.increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, sai):
        self.increment = sai/self.salary

e = Employee()
print("Base Salary :", e.salary)
print("Increment by Salary :", e.salaryAfterIncrement)
print(e.increment)
e.salaryAfterIncrement = 9000
print(e.increment)







