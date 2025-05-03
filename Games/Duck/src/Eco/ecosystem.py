from random import choice  #, randint
from Eco.interfaces import IObserver
from Eco.BirdFactory import createBird
from Eco.HumanFactory import createHuman
from Eco.PredatorFactory import createPredator
from Eco.lake import Lake
from Eco.bird import BirdAttributes
from Eco.human import GadgetAttributes
from Eco.predator import PredatorAttributes


class Habitant(IObserver):
    habitantDict = {
        "empty": {
            "name": "Empty",
            "id": "*",
            "dominance": 0
        },
        "Bird": {
            "name": "Bird",
            "id": "B",
            "dominance": 2
        },
        "Human": {
            "name": "Human",
            "id": "H",
            "dominance": 8
        }
    }
    habitantTypes = list(habitantDict.keys())   # Mammel, Predator

    def __init__(self, type):
        self.habitant = Habitant.habitantDict[type]

    def update(self):
        pass

    def getDescription(self):
        pass

    def getDanger(self):
        pass

    def id(self):
        return self.habitant["id"] 

class Patch():

    patchDict = {
        "Forrest": {
            "name": "Forrest",
            "id": "F",
            "color": "32m",
            "view": 2
        },
        "Water": {
            "name": "Water",
            "id": "W",
            "color": "34m",
            "view": 8
        },
        "Beach": {
            "name": "Beach",
            "id": "B",
            "color": "33m",
            "view": 7
        }
    }
    patchTypes = list(patchDict.keys())  # Beach, Gras

    def __init__(self, type):
        self.patch = Patch.patchDict[type]
        self.habitant: Habitant = Habitant("empty")

    def id(self):
        return self.patch["id"]

    def color(self):
        return self.patch["color"]

    def habitantid(self):
        return self.habitant.id()
 
class Ecosystem():
    def __init__(self, y: int, x: int):
        #old constructor
        self.lakeCapacity = x
        self.p = Lake(self.lakeCapacity, False)
        self.ecoList: list[IObserver] = []

        #new constructor
        self.y = y # zeile
        self.x = x # spalte
        self.grid = [[Patch(choice(Patch.patchTypes)) for _ in range(x)]for _ in range(y)] # y spalte (aussen), x zeile (innen)

    def populateEcosystem(self):
        # old population
        # define habitants of the ecosystem
        for i in range(self.lakeCapacity - 2):
            bird = createBird(choice(BirdAttributes.birdList))
            self.ecoList.append(bird)
        self.ecoList.append(createHuman(choice(GadgetAttributes.gadgetList)))
        pa = PredatorAttributes.gadgetList
        self.ecoList.append(createPredator(choice(pa)))
        # populate lake with ecoList habitants and notify all observers
        for habitant in self.ecoList:
            self.p.registerObserver(habitant, 1)
            print(habitant.getDescription())
        self.p.notifyObservers()

        # new population
        for y in range(len(self.grid)):
            zeile = []
            for x in range(len(self.grid[y])):
                self.grid[y][x].habitant = Habitant(choice(Habitant.habitantTypes))

    def plotEcosystem(self):
        for y in range(len(self.grid)):
            zeile = []
            for x in range(len(self.grid[y])):
                patchcolor = self.grid[y][x].color()
                symbol = self.grid[y][x].habitantid() or "="
                zeile.append("\033[" + patchcolor + symbol + "\033[0m")
            print(" ".join(zeile))

    def lapEcosystem():
        pass


e = Ecosystem(3, 5)
e.plotEcosystem()
e.populateEcosystem()
e.plotEcosystem()
