from dataclasses import dataclass
from interfaces import IObserver, IFlyBehavior, IQuackBehavior


@dataclass
class BirdAttributes:
    birdList = ["duck", "gull", "swan"]


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
        return "quack"


class Squawk(IQuackBehavior):

    def quack(self):
        return "squawk"


class Honk(IQuackBehavior):

    def quack(self):
        return "honk"


class Bird(IObserver):

    def __init__(self, lake):
        self.bird = "bird"
        self.lake = lake    # have a reference for de-register
        self.lake.registerObserver(self)
        self.quackBehavior: IQuackBehavior()
        self.flyBehavior: IFlyBehavior()

    def update(self):
        if (self.lake.getPredator()):
            self.flyBehavior = Fly()
        else:
            self.flyBehavior = Swim()

        print("Bird is " + self.bird + " - " + self.flyBehavior.fly() + " - " + self.quackBehavior.quack())

    def performQuack(self):
        return self.quackBehavior.quack()

    def performFly(self):
        return self.flyBehavior.fly()

    def setFlyBehavior(self, fb):
        self.flyBehavior = fb


class Duck(Bird):

    def __init__(self, lake):
        super().__init__(lake)
        self.bird = "Duck"

    quackBehavior = Quack()
    flyBehavior = Fly()


class Gull(Bird):

    def __init__(self, lake):
        super().__init__(lake)
        self.bird = "Gull"

    quackBehavior = Squawk()
    flyBehavior = NoFly()


class Swan(Bird):

    def __init__(self, lake):
        super().__init__(lake)
        self.bird = "Swan"

    quackBehavior = Honk()
    flyBehavior = NoFly()
