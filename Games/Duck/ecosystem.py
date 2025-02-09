from random import choice, randint
from lake import Lake
from bird import BirdAttributes, Duck, Gull, Swan
from human import Human, Foto, Gun
from predator import Predator

lakeCapacity = 8
p = Lake(lakeCapacity, False)
ecoList = []

# define habitants of the ecosystem
for i in range(lakeCapacity - 2):
    match choice(BirdAttributes.birdList):
        case "duck":
            bird = Duck(p)
        case "gull":
            bird = Gull(p)
        case "swan":
            bird = Swan(p)
    ecoList.append(bird)

w = Predator(p)
h = Human(p)
h_f = Foto(p, h)
h_f_g = Gun(p, h_f)
ecoList.append(h_f)

# populate lake with ecoList habitants and notify all observers
for habitant in ecoList:
    habitant.registerObserver()

p.notifyObservers()

# w.registerObserver()
h_f_g.registerObserver()

p.notifyObservers()
