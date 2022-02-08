from abc import ABCMeta, abstractclassmethod
from typing import List


# Command
class Order(metaclass=ABCMeta):
    @abstractclassmethod
    def execute(self):
        pass


# Concret Command
class BuyOrder(Order):
    def __init__(self, stock) -> None:
        self.stock = stock

    def execute(self):
        self.stock.buy()


class SellOrder(Order):
    def __init__(self, stock) -> None:
        self.stock = stock

    def execute(self):
        self.stock.sell()


# Receiver
class Stock:
    def buy(self):
        print("Executing buy order...")

    def sell(self):
        print("Executing sell order...")


# Invoker
class Agent:
    def __init__(self) -> None:
        self.__orders_queue: List = []

    def add_order_to_queue(self, order):
        self.__orders_queue.append(order)
        order.execute()


if __name__ == "__main__":
    stock = Stock()

    sell_order = SellOrder(stock=stock)
    buy_order = BuyOrder(stock=stock)

    agent = Agent()

    agent.add_order_to_queue(sell_order)
    agent.add_order_to_queue(buy_order)
