print("Multiple Inheritance")


class Father:
    def __init__(self):
        super().__init__()
        print("Father Constructor")

    def ShowF(self):
        print("Father class Method")


class Mother:
    def __init__(self):
        super().__init__()
        print("Mother Constructor")

    def ShowM(self):
        print("Mother Method")


class Son(Father, Mother):
    def __init__(self):
        super().__init__()
        print("Son constructor")

    def ShowS(self):
        print("Son Method ")


S = Son()
S.ShowF()
S.ShowM()
S.ShowS()



