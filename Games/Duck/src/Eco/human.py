from dataclasses import dataclass
from Eco.interfaces import IObserver, IDecorator


@dataclass
class GadgetAttributes:
    gadgetList = ["foto", "gun", "bag"]


class Human(IObserver):
    def __init__(self):
        self.description = "I'm human"
        self.danger = 3

    def getDescription(self):
        return self.description

    def getDanger(self):
        return self.danger

    def update(self, lakedanger):
        print(self.getDescription())


class Gadget(IDecorator, IObserver):

    def __init__(self, human: Human):
        self._human = human

    def update(self, lakedanger):
        print(self.getDescription())

    def getDescription(self):
        return self._human.getDescription()

    def getDanger(self):
        return self._human.getDanger()


class Foto(Gadget):

    def getDescription(self):
        return self._human.getDescription() + ", foto"

    def getDanger(self):
        return self._human.getDanger() + 1


class Gun(Gadget):

    def getDescription(self):
        return self._human.getDescription() + ", gun"

    def getDanger(self):
        return self._human.getDanger() + 5


class Bag(Gadget):

    def getDescription(self):
        return self._human.getDescription() + ", bag"

    def getDanger(self):
        return self._human.getDanger() + 1
