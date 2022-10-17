class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def Displaye(self):
        print("*********")
        print(f"The name of the {self.name}")
        print(f"The seats available in the train are :{self.seats}")
        print("**********")

    def fareInfo(self):
        print(f"The price of the tikit is :Tk {self.fare}")

    def bookticket(self):
        if(self.seats>0):
            print(f"Your ticket has been booked! your set number is {self.seats}")
            self.seats=self.seats-1
        else:
            print("Sorry this train is full kindly try is tatkal")

    def cancelTiket(self):
        self.seats=self.seats+1
        print("Cencel seats ! and Added 1 site by train")

intercity=Train("Intercity Express :1200",90,2)
intercity.Displaye()
intercity.bookticket()
intercity.bookticket()
intercity.cancelTiket()
intercity.bookticket()
intercity.fareInfo()
