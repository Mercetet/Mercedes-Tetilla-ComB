class Account:
    def __init__(self, holder, quantity):
        self.__holder = holder
        self.__quantity = quantity

    @property
    def holder(self):
        return self.__holder

    @holder.setter
    def holder(self, new_at):
        self.__holder = new_at

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, new_at):
        self.__quantity = new_at

    def show(self):
        print(f"{self.__holder}, {self.__quantity}")

    def deposit(self, money):
        if(money > 0):
            self.__quantity += money
        return self.__quantity

    def withdraw(self, money):
        if(money > 0):
            self.__quantity -= money
        return self.__quantity
