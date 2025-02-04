from abc import ABC
from observer import IObserver


class IHuman(ABC):

    def getDescription(self):
        return self.description


class Human(IHuman, IObserver):
    def __init__(self, pont):
        self.pont = pont
        self.pont.registerObserver(self)
        self.description = "human at lake"

    def update(self):
        print(self.description)


class Gadget(IHuman):
    pass
