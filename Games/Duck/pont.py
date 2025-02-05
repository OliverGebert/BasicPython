from interfaces import ISubject


class Pont(ISubject):

    def __init__(self, cap, pred):
        self.capacity = int(cap)
        self.predator = bool(pred)
        self.ducklist = []

    def registerObserver(self, duck):
        if (len(self.ducklist) < self.capacity):
            self.ducklist.append(duck)

    def removeObserver(self, duck):
        # missing implementation of removing ducks from pont,
        # also test_removeObserver not implemented
        pass

    def notifyObservers(self):
        print("Predator status: " + str(self.predator))
        for d in self.ducklist:
            d.update()

    def count(self):
        return len(self.ducklist)

    def getPredator(self):
        return self.predator

    def setPredator(self, pred):
        self.predator = pred

    def setCapacity(self, cap):
        self.capacity = cap
