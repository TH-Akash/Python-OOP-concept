class Calculate:
    def __init__(self, number):
        self.number = number

    def square(self):
        print(f"The value of {self.number} square is {self.number**2}")

    @staticmethod
    def greed():
        print("Hello there welcome to the best calculate of the world")

Result = Calculate(8) 
Result.square()
Result.greed()