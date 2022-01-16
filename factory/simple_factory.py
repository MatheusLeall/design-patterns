from abc import ABCMeta, abstractmethod
from typing import List


class Animal(metaclass=ABCMeta):
    @abstractmethod
    def action(self: object):
        pass


class Dog(Animal):
    def action(self: object) -> None:
        print("\nThe dog goes Woof!\n")


class Cat(Animal):
    def action(self: object) -> None:
        print("\nThe cat goes Meooow!\n")


class Fox(Animal):
    def action(self: object) -> None:
        print("\nAccess to discovery: https://www.youtube.com/watch?v=jofNR_WkoCE&ab_channel=discoveryplusNorge\n")


# Factory
class Factory:
    def create_animal(self: object, type: str) -> Animal:
        return eval(type)().action()


# Client
if __name__ == "__main__":
    factory: Factory = Factory()
    supported_animals: List[str] = ["Dog", "Cat", "Fox"]

    animal: str = input("which animal do you want to know the action? [Dog, Cat, Fox]: ").capitalize()

    if animal not in supported_animals:
        raise ValueError("The animal not exists!")

    factory.create_animal(animal)
