from dataclasses import dataclass
from interfaces import IObserver, IFlyBehavior, IQuackBehavior


@dataclass
class BirdAttributes:
    birdlist = ["duck", "gull", "swan"]
    colorList = ["green", "brown", "orange", "blue", "white", "black"]
    typeList = ["male", "female"]


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


class Bird(IObserver):

    def __init__(self, color, type, lake):
        self.color = str(color)
        self.type = str(type)
        self.lake = lake    # have a reference for de-register
        self.lake.registerObserver(self)
        self.quackBehavior: IQuackBehavior()
        self.flyBehavior: IFlyBehavior()

    def update(self):
        if (self.lake.getPredator()):
            self.flyBehavior = Fly()
        else:
            self.flyBehavior = Swim()

        print("Bird has color " + self.color + " - " + self.flyBehavior.fly())

    def performQuack(self):
        return self.quackBehavior.quack()

    def performFly(self):
        return self.flyBehavior.fly()

    def setFlyBehavior(self, fb):
        self.flyBehavior = fb


class RealBird(Bird):

    quackBehavior = Quack()
    flyBehavior = Fly()


class RubberBird(Bird):

    quackBehavior = Quick()
    flyBehavior = NoFly()


class WoodenBird(Bird):

    quackBehavior = Quiet()
    flyBehavior = NoFly()
