from interfaces import IObserver


class Predator(IObserver):
    def __init__(self, lake):
        self.lake = lake
        self.description = "I'm a predator"
        self.danger = 10

    def registerObserver(self):
        self.lake.registerObserver(self, self.getDanger())

    def getDescription(self):
        return self.description

    def getDanger(self):
        return self.danger

    def update(self, lakeDanger):
        print(self.getDescription())
