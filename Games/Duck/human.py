from interfaces import IObserver, IDecorator


class Human(IDecorator, IObserver):
    def __init__(self, lake):
        self.lake = lake
        self.description = "I'm human"
        self.danger = 3

    def registerObserver(self):
        self.lake.registerObserver(self, self.getDanger())

    def getDescription(self):
        return self.description

    def getDanger(self):
        return self.danger

    def update(self, lakedanger):
        print(self.getDescription())


class Gadget(IDecorator, IObserver):

    def __init__(self, lake, human: IDecorator):
        self._human = human
        self.lake = lake

    def update(self, lakedanger):
        print(self.getDescription())

    def registerObserver(self):
        self.lake.registerObserver(self, self.getDanger())

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
