from dataclasses import dataclass
from Eco.interfaces import IObserver, IBirdBehavior


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
        self.danger = 1

    def registerObserver(self):
        self.lake.registerObserver(self, self.getDanger())

    def getDescription(self):
        return self.description

    def getDanger(self):
        return self.danger

    def performQuack(self):
        return "---"

    def performMove(self):
        return self.moveBehavior.move()

    def update(self, lakedanger):
        if lakedanger > 10:
            self.moveBehavior = Fly()
        print("Bird is " + self.getDescription() + " - " + self.performMove() + " - " + self.performQuack())


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
