from interfaces import IObserver, IDecorator


class Human(IDecorator, IObserver):
    def __init__(self, pont):
        self.pont = pont
        self.pont.registerObserver(self)
        self.description = "I'm human"

    def update(self):
        print(self.getDescription())

    def getDescription(self):
        return self.description


class Gadget(IDecorator, IObserver):

    def __init__(self, pont, human: IDecorator):
        self._human = human
        self.pont = pont
        self.pont.registerObserver(self)

    def update(self):
        print(self.getDescription())

    def getDescription(self):
        return self._human.description


class Foto(Gadget):

    def getDescription(self):
        return self._human.getDescription() + ", foto"


class Gun(Gadget):

    def getDescription(self):
        return self._human.getDescription() + ", gun"
