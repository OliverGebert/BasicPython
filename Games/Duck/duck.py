from abc import ABC, abstractmethod
from dataclasses import dataclass
from interfaces import IObserver, IFlyBehavior, IQuackBehavior


class Swim(IFlyBehavior):

    def fly(self):
        return "I swim"


class Fly(IFlyBehavior):

    def fly(self):
        return "I fly"


class FlyPropeller(IFlyBehavior):

    def fly(self):
        return "I fly with an propeller"


class NoFly(IFlyBehavior):

    def fly(self):
        return "I cannot fly"


class Quack(IQuackBehavior):

    def quack(self):
        return "quaaak"


class Quick(IQuackBehavior):

    def quack(self):
        return "quiiik"


class Quiet(IQuackBehavior):

    def quack(self):
        return "---"


@dataclass
class DuckAttributes:
    colorList = ["green", "brown", "orange", "blue", "white", "black"]
    typeList = ["male", "female"]


class Duck(IObserver):

    def __init__(self, color, type, pont):
        self.color = str(color)
        self.type = str(type)
        self.pont = pont    # have a reference for de-register
        self.pont.registerObserver(self)
        self.quackBehavior: IQuackBehavior()
        self.flyBehavior: IFlyBehavior()

    def update(self):
        if (self.pont.getPredator()):
            self.flyBehavior = Fly()
        else:
            self.flyBehavior = Swim()

        print("Duck has color " + self.color + " - " + self.flyBehavior.fly())

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
