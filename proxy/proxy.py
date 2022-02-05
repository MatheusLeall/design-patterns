from abc import ABCMeta, abstractclassmethod


# Interface
class Wallet(metaclass=ABCMeta):
    @abstractclassmethod
    def pay(self):
        pass


# Real Object
class Bank(Wallet):
    def __init__(self) -> None:
        self.card = None
        self.account = None

    def __get_account(self):
        self.account = self.card
        return self.account

    def __has_ammount(self):
        print(f"\nBank :: Checking if account {self.__get_account()} has money.")
        return True

    def set_card(self, card):
        self.card = card

    def pay(self):
        if self.__has_ammount():
            print("Bank :: Pay something...\n")
            return True
        else:
            print("Bank :: Sorry, you don't have money to pay something.\n")
            return False


# Proxy
class DebitCard(Wallet):
    def __init__(self) -> None:
        self.bank = Bank()

    def pay(self):
        card = int(input("Proxy :: Entrer the card number: "))
        self.bank.set_card(card=card)
        return self.bank.pay()


# Client
class Client:
    def __init__(self) -> None:
        print("Client :: I want to buy a beer!\n")
        self.debit_card = DebitCard()
        self.bought = None

    def payment(self):
        self.bought = self.debit_card.pay()

    def __del__(self):
        if self.bought:
            print("Client :: I'll be able to buy a beer!!!\n")
        else:
            print("Client :: I won't be able to buy the beer :(\n")


if __name__ == "__main__":
    client = Client()
    client.payment()
