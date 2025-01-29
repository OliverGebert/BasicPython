from random import choice
from duck import RealDuck, DuckAttributes
from pont import Pont

systemLaps = 10
pontCapacity = 5
pontPredator = False
p = Pont(pontCapacity, pontPredator)

for lap in range(systemLaps):

    if (p.count() < pontCapacity):
        color = choice(DuckAttributes.colorList)
        type = choice(DuckAttributes.typeList)
        d = RealDuck(color, type)
        p.registerObserver(d)

    print("Lap #", lap)
    p.notifyObservers()
