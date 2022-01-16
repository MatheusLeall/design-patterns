from abc import ABCMeta, abstractmethod
from typing import Any, Optional


# Abstract Factory
class PizzaFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_vegan_pizza(self: object) -> None:
        pass

    @abstractmethod
    def create_pizza(self: object) -> None:
        pass


# Concret Factory A
class BrazilianPizza(PizzaFactory):
    def create_vegan_pizza(self: object):
        return AuberguinePizza()

    def create_pizza(self: object):
        return MozzarellaPizza()


# Concret Factory B
class ItalianPizza(PizzaFactory):
    def create_vegan_pizza(self: object):
        return BroccoliPizza()

    def create_pizza(self: object):
        return MargheritaPizza()


# Abstract Product A
class VeganPizza(metaclass=ABCMeta):
    @abstractmethod
    def prepare(self: object):
        pass


# Abstract Product B
class Pizza(metaclass=ABCMeta):
    @abstractmethod
    def serve(self: object, VeganPizza):
        pass


# Concret Product
class AuberguinePizza(VeganPizza):
    def prepare(self: object):
        print(f"Preparing {type(self).__name__}")


class MozzarellaPizza(Pizza):
    def serve(self: object, VeganPizza):
        print(f"Serving {type(self).__name__} with {type(VeganPizza).__name__}")


class BroccoliPizza(VeganPizza):
    def prepare(self: object):
        print(f"Preparing {type(self).__name__}")


class MargheritaPizza(Pizza):
    def serve(self: object, VeganPizza):
        print(f"Serving {type(self).__name__} with {type(VeganPizza).__name__}")


# Client
class Pizzaria:
    def cook_pizza(self: object):
        for factory in (BrazilianPizza(), ItalianPizza()):
            self.factory = factory
            self.pizza = self.factory.create_pizza()
            self.pizza_veg = self.factory.create_vegan_pizza()
            self.pizza_veg.prepare()
            self.pizza.serve(self.pizza_veg)


pizzaria = Pizzaria()
pizzaria.cook_pizza()
