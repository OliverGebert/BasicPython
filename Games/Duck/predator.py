from interfaces import IObserver
from dataclasses import dataclass


@dataclass
class PredatorAttributes:
    gadgetList = ["wolf", "fox"]


class Predator(IObserver):
    def __init__(self, lake):
        self.lake = lake
        self.description = "I'm a predator"
        self.danger = 0

    def registerObserver(self):
        self.lake.registerObserver(self, self.getDanger())

    def getDescription(self):
        return self.description

    def getDanger(self):
        return self.danger

    def update(self, lakeDanger):
        print(self.getDescription())


class Wolf(Predator):
    def __init__(self, lake):
        super().__init__(lake)
        self.description = "I'm a wolf"
        self.danger = 10


class Fox(Predator):
    def __init__(self, lake):
        super().__init__(lake)
        self.description = "I'm a fox"
        self.danger = 6
