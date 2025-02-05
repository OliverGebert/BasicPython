from interfaces import IObserver, IDecorator


class Hunter(IDecorator, IObserver):
    def __init__(self, pont):
        self.pont = pont
        self.pont.registerObserver(self)
        self.description = "I'm hunter"

    def update(self):
        print(self.getDescription())

    def getDescription(self):
        return self.description


class Gadget(IDecorator, IObserver):

    def __init__(self, pont, hunter: IDecorator):
        self._hunter = hunter
        self.pont = pont
        self.pont.registerObserver(self)

    def update(self):
        print(self.getDescription())

    def getDescription(self):
        return self._hunter.description


class Foto(Gadget):

    def getDescription(self):
        return self._hunter.getDescription() + ", foto"


class Gun(Gadget):

    def getDescription(self):
        return self._hunter.getDescription() + ", gun"
