print("Multilevel Inheritance ")

class Persone:
    country="Bangladesh"
    def takeBraeth(self):
        print("I am a Persone class Parent ")


class Employe(Persone):
    company="Viva Soft"
    def takeBraeth(self):
        print("I am Employee Class ,Persone class child")

    def getSalary(self):
        print(f" Salary is {self.salary}")

class Programmer(Employe):
    company = "Fiver"

    def getSalary(self):
        print(f"No Salary to Programmer")

    def takeBraeth(self):
        print("I am  a Programmer Class, Employee class child")


p=Persone()
p.takeBraeth()
e=Employe()
e.takeBraeth()
print(e.company)
pr=Programmer()
pr.takeBraeth()
print(pr.company)
print(pr.country)