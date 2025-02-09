from interfaces import IObserver, IDecorator


class Human(IDecorator, IObserver):
    def __init__(self, lake):
        self.lake = lake
        self.description = "I'm human"

    def update(self):
        print(self.getDescription())

    def registerObserver(self):
        self.lake.registerObserver(self)

    def getDescription(self):
        return self.description


class Gadget(IDecorator, IObserver):

    def __init__(self, lake, human: IDecorator):
        self._human = human
        self.lake = lake

    def update(self):
        print(self.getDescription())

    def registerObserver(self):
        self.lake.registerObserver(self)

    def getDescription(self):
        return self._human.getDescription()


class Foto(Gadget):

    def getDescription(self):
        return self._human.getDescription() + ", foto"


class Gun(Gadget):

    def getDescription(self):
        return self._human.getDescription() + ", gun"
