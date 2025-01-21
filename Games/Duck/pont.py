from abc import ABC, abstractmethod
from duck import IObserver


class ISubject(ABC):
    @abstractmethod
    def registerObserver(o: IObserver):
        pass

    @abstractmethod
    def removeObserver(o: IObserver):
        pass

    @abstractmethod
    def notifyObservers():
        pass


class Pont(ISubject):

    def __init__(self, cap, pred):
        self.capacity = int(cap)
        self.predator = bool(pred)
        self.ducklist = []

    def registerObserver(self, duck):
        self.ducklist.append(duck)

    def removeObserver(self, duck):
        pass

    def notifyObservers(self):
        for d in self.ducklist:
            d.update()

    def count(self):
        return len(self.ducklist)

    def changePredator(self, pred):
        self.predator = pred

    def changeCapacity(self, cap):
        self.capacity = cap
