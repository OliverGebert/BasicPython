from abc import ABC, abstractmethod
from dataclasses import dataclass


class IFlyBehavior(ABC):
    @abstractmethod
    def fly(self):
        pass


class Fly(IFlyBehavior):

    def fly(self):
        return "I fly"


class FlyPropeller(IFlyBehavior):

    def fly(self):
        return "I fly with an propeller"


class NoFly(IFlyBehavior):

    def fly(self):
        return "I cannot fly"


class IQuackBehavior(ABC):
    @abstractmethod
    def quack(self):
        pass


class Quack(IQuackBehavior):

    def quack(self):
        return "quaaak"


class Quick(IQuackBehavior):

    def quack(self):
        return "quiiik"


class Quiet(IQuackBehavior):

    def quack(self):
        return "---"


class IObserver(ABC):
    @abstractmethod
    def update(self):
        pass


@dataclass
class DuckAttributes:
    colorList = ["green", "brown", "orange", "blue", "white", "black"]
    typeList = ["male", "female"]


class Duck(IObserver):

    def __init__(self, color, type):
        self.color = str(color)
        self.type = str(type)
        self.quackBehavior: IQuackBehavior()
        self.flyBehavior: IFlyBehavior()

    def update(self):
        print("Duck has color " + self.color + " - Duck from type " + self.type)

    def performQuack(self):
        return self.quackBehavior.quack()

    def performFly(self):
        return self.flyBehavior.fly()

    def setFlyBehavior(self, fb):
        self.flyBehavior = fb


class RealDuck(Duck):

    quackBehavior = Quack()
    flyBehavior = Fly()


class RubberDuck(Duck):

    quackBehavior = Quick()
    flyBehavior = NoFly()


class WoodenDuck(Duck):

    quackBehavior = Quiet()
    flyBehavior = NoFly()
