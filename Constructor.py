print("Super constructor :  ")

class Persone:
    country="Bangladesh"

    def __init__(self):
        print("Initialize Person constructor 1111 ")

    def takeBraeth(self):
        print("I am a Persone class Parent -------")


class Employe(Persone):
    company="Viva Soft"

    def __init__(self):
        super().__init__()
        print("Initialize Employee constructor 2222 ")

    def takeBraeth(self):

        print("I am Employee Class ,Persone class child ******")

    def getSalary(self):
        print(f" Salary is {self.salary}")

class Programmer(Employe):
    company = "Fiver"

    def __init__(self):
        super().__init__()
        print("Initialize Programmer constructor 33333 ")

    def getSalary(self):
        print(f"No Salary to Programmer")

    def takeBraeth(self):

        print("I am  a Programmer Class, Employee class child")


p=Persone()


e=Employe()

# print(e.company)

pr=Programmer()

