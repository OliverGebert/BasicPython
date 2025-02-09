from interfaces import IObserver


class Predator(IObserver):
    def __init__(self, lake):
        self.lake = lake
        self.description = "I'm a predator"

    def update(self):
        print(self.getDescription())

    def registerObserver(self):
        self.lake.registerObserver(self)

    def getDescription(self):
        return self.description
