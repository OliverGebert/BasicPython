from random import choice, randint
from bird import BirdAttributes, Duck, Gull, Swan
from lake import Lake
from human import Human, Foto, Gun

systemLaps = 10
lakeCapacity = 6
p = Lake(lakeCapacity, False)

for lap in range(systemLaps):

    if (p.count() < lakeCapacity - 3):
        # problem: even if no space in lake left, object is instanciated
        match choice(BirdAttributes.birdList):
            case "duck":
                bird = Duck(p)
            case "gull":
                bird = Gull(p)
            case "swan":
                bird = Swan(p)

    print("Lap #" + str(lap))
    p.setPredator(bool(randint(0, 1)))
    p.notifyObservers()

h = Human(p)
h_f = Foto(p, h)
h_f_g = Gun(p, h_f)
p.notifyObservers()
