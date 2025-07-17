class Computer:
    def __init__(self):
       self.__maxprice = 600

    def sell(self):
        print("Selling price of computer", self.__maxprice)

    def setmaxprice(self,price):
        self.__maxprice = price

com = Computer()
com.sell()
com.__maxprice = 500
com.sell()
com.setmaxprice(800)
com.sell()