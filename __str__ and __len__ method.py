print("Str method ")
class Number:

    def __init__(self,num):
        self.num = num
    # Str method overloading

    def __str__(self):
        return f"Decimal Number {self.num}"

    def __len__(self):
        return 1

n = Number(9)
print(n)
print(len(n))
