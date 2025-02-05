from abc import ABC, abstractmethod


class IObserver(ABC):

    @abstractmethod
    def update(self, b):
        pass


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


class IDecorator(ABC):

    @abstractmethod
    def getDescription(self):
        pass


class IFlyBehavior(ABC):
    @abstractmethod
    def fly(self):
        pass


class IQuackBehavior(ABC):
    @abstractmethod
    def quack(self):
        pass
