print("Multiple Inheritance ")

class Employee:
    company = "Visa" 
    eCode = 120

class Frelancer:
    company = "fiver"
    level = 0
    def upgradeLevel(self):
        self.level = self.level = 1

class Programmer(Employee,Frelancer):
    name = "Tanvir"


p = Programmer()
print(p.company)
p.upgradeLevel()
print(p.level)
