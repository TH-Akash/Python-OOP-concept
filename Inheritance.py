print("Inheritance OOP")

class Empolyee:
    company="Google"

    def showDetalis(self):
        print("This is Employee")

class Programmer(Empolyee):
    language="Python"
    company = "Youtube"

    def getLanguage(self):
        print(f"The language is {self.language} ")

    def showDetalis(self):
        print("I am Programmer Class")

e = Empolyee()
e.showDetalis()
p = Programmer()
p.showDetalis()
# print(p.company) Parent class er Attribute
print(p.company)

