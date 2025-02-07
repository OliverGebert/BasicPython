from interfaces import IObserver, IDecorator


class Human(IDecorator, IObserver):
    def __init__(self, lake):
        self.lake = lake
        self.lake.registerObserver(self)
        self.description = "I'm human"

    def update(self):
        print(self.getDescription())

    def getDescription(self):
        return self.description


class Gadget(IDecorator, IObserver):

    def __init__(self, lake, human: IDecorator):
        self._human = human
        self.lake = lake
        self.lake.registerObserver(self)

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
