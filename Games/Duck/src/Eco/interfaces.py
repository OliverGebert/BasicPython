from abc import ABC, abstractmethod


class IObserver(ABC):

    @abstractmethod
    def update(self, b):
        pass

    @abstractmethod
    def getDescription(self):
        pass

    @abstractmethod
    def getDanger(self):
        pass


class ISubject(ABC):
    @abstractmethod
    def registerObserver(o: IObserver):
        pass

    @abstractmethod
    def removeObserver(o: IObserver):
        pass

    @abstractmethod
    def notifyObservers(self):
        pass


class IDecorator(ABC):

    @abstractmethod
    def getDescription(self):
        pass


class IBirdBehavior(ABC):
    @abstractmethod
    def move(self):
        pass
