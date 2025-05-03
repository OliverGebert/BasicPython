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
    def __init__(self):
        self.description = "bird"
        self.moveBehavior: IBirdBehavior()
        self.danger = 1

    def getDescription(self):
        result = self.description + " and " + self.moveBehavior.move()
        return result

    def getDanger(self):
        return self.danger

    def performQuack(self):
        return "---"

    def performMove(self):
        return self.moveBehavior.move()

    def update(self, lakedanger):
        pass


class Duck(Bird):

    def __init__(self):
        super().__init__()
        self.description = "Duck"

    def performQuack(self):
        return "quack"

    moveBehavior = Fly()


class Gull(Bird):

    def __init__(self):
        super().__init__()
        self.description = "Gull"

    def performQuack(self):
        return "squawk"

    moveBehavior = Walk()


class Swan(Bird):

    def __init__(self):
        super().__init__()
        self.description = "Swan"

    def performQuack(self):
        return "honk"

    moveBehavior = Swim()
