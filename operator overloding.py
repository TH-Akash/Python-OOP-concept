print("operator overloading of python ")

class Number:
    def __init__(self, num):
        self.num = num

    # added number overloading
    def __add__(self, num2):
        print("Lets Add")
        return self.num + num2.num

    # multiple number
    def __mul__(self, num2):
        return self.num*num2.num

n1 = Number(6)
n2 = Number(3)
sum = n1+n2
mul = n1 * n2
print(sum)
print(mul)