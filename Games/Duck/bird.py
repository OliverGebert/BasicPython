from dataclasses import dataclass
from interfaces import IObserver, IBirdBehavior


@dataclass
class BirdAttributes:
    birdList = ["duck", "gull", "swan"]


class Swim(IBirdBehavior):

    def move(self):
        return "I swim"


class Fly(IBirdBehavior):

    def move(self):
        return "I fly"


class Walk(IBirdBehavior):

    def move(self):
        return "I walk"


class Bird(IObserver):

    def __init__(self, lake):
        self.description = "bird"
        self.lake = lake    # have a reference for de-register
        self.moveBehavior: IBirdBehavior()

    def getDescription(self):
        return self.description

    def update(self):
        print("Bird is " + self.description + " - " + self.moveBehavior.move() + " - " + self.performQuack())

    def registerObserver(self):
        self.lake.registerObserver(self)

    def performQuack(self):
        return "---"

    def performFly(self):
        return self.moveBehavior.move()

    def setFlyBehavior(self, fb):
        self.moveBehavior = fb


class Duck(Bird):

    def __init__(self, lake):
        super().__init__(lake)
        self.description = "Duck"

    def performQuack(self):
        return "quack"

    moveBehavior = Fly()


class Gull(Bird):

    def __init__(self, lake):
        super().__init__(lake)
        self.description = "Gull"

    def performQuack(self):
        return "squawk"

    moveBehavior = Walk()


class Swan(Bird):

    def __init__(self, lake):
        super().__init__(lake)
        self.description = "Swan"

    def performQuack(self):
        return "honk"

    moveBehavior = Swim()
