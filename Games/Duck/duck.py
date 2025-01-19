from abc import ABC, abstractmethod


class FlyBehavior(ABC):
    @abstractmethod
    def fly(self):
        pass


class Fly(FlyBehavior):

    def fly(self):
        return "I fly"


class NoFly(FlyBehavior):

    def fly(self):
        return "I cannot fly"


class QuackBehavior(ABC):
    @abstractmethod
    def quack(self):
        pass


class Quack(QuackBehavior):

    def quack(self):
        return "quaaak"


class Quick(QuackBehavior):

    def quack(self):
        return "quiiik"


class Quiet(QuackBehavior):

    def quack(self):
        return "---"


class Duck(ABC):

    def __init__(self, color, type):
        self.color = str(color)
        self.type = str(type)
        self.quackBehavior: QuackBehavior()
        self.flyBehavior: FlyBehavior()

    def draw(self):
        return "Duck has color " + self.color + "/nDuck from type " + self.type

    def performQuack(self):
        return self.quackBehavior.quack()

    def performFly(self):
        return self.flyBehavior.fly()


class RealDuck(Duck):

    quackBehavior = Quack()
    flyBehavior = Fly()


class RubberDuck(Duck):

    quackBehavior = Quick()
    flyBehavior = NoFly()


class WoodenDuck(Duck):

    quackBehavior = Quiet()
    flyBehavior = NoFly()
