class Universities:
    def __init__(self, fillial):
        self.fillial = fillial

    def nameOfFillials(self):
        return f'there are names: {self.fillial}'

univer1 = Universities("MGU")
print(univer1.nameOfFillials())
# bank
class Bank:
    def __init__(self, cardNumber, cash):
        self.cardNumber = cardNumber
        self.__cash = cash      
    def user(self):
        return f'card number is {self.cardNumber} and cash is {self.cash}' 
    def check(self):
        if self.cash >= 0:
            print(f'your cash is {self.cash} you can buy everything')
        else:
            print("you do not have enough money")
user1bank = Bank(3533465235, 1000)
user2bank = Bank(456435765243, -10)
print(user1bank.user())
print(user1bank.check())
print(user2bank.user())
print(user2bank.check())