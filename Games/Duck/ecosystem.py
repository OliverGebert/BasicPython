from random import choice, randint
from BirdFactory import createBird
from HumanFactory import createHuman
from lake import Lake
from bird import BirdAttributes
from human import GadgetAttributes
from predator import Predator

lakeCapacity = 8
p = Lake(lakeCapacity, False)
ecoList = []

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

# w = Predator(p)
# w.registerObserver()
