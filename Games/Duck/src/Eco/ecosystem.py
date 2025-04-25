from random import choice  #, randint
from Eco.interfaces import IObserver
from Eco.BirdFactory import createBird
from Eco.HumanFactory import createHuman
from Eco.PredatorFactory import createPredator
from Eco.lake import Lake
from Eco.bird import BirdAttributes
from Eco.human import GadgetAttributes
from Eco.predator import PredatorAttributes

lakeCapacity = 8
p = Lake(lakeCapacity, False)
ecoList: list[IObserver] = []

# define habitants of the ecosystem
for i in range(lakeCapacity - 2):
    bird = createBird(p, choice(BirdAttributes.birdList))
    ecoList.append(bird)

# populate lake with ecoList habitants and notify all observers
for habitant in ecoList:
    habitant.registerObserver()
p.notifyObservers()

# create hunman and notify al lobservers again
human = createHuman(p, choice(GadgetAttributes.gadgetList))
human.registerObserver()
p.notifyObservers()

# create predator and notify al lobservers again
pa = PredatorAttributes.gadgetList
predator = createPredator(p, choice(pa))
predator.registerObserver()
p.notifyObservers()
