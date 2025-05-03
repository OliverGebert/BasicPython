from random import choice  #, randint
from Eco.interfaces import IObserver
from Eco.BirdFactory import createBird
from Eco.HumanFactory import createHuman
from Eco.PredatorFactory import createPredator
from Eco.lake import Lake
from Eco.bird import BirdAttributes
from Eco.human import GadgetAttributes
from Eco.predator import PredatorAttributes


class Ecosystem():
    def __init__(self, size: int):
        self.lakeCapacity = size
        # self.lakeCapacity = 8
        self.p = Lake(self.lakeCapacity, False)
        self.ecoList: list[IObserver] = []

    def populateEcosystem(self):
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
        pass

    def lapEcosystem():
        pass

e = Ecosystem(12)
e.populateEcosystem()
