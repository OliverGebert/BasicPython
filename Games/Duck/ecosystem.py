from random import choice, randint
from duck import RealDuck, DuckAttributes
from pont import Pont

systemLaps = 10
pontCapacity = 5
p = Pont(pontCapacity, False)

for lap in range(systemLaps):

    if (p.count() < pontCapacity):
        color = choice(DuckAttributes.colorList)
        type = choice(DuckAttributes.typeList)
        d = RealDuck(color, type, p)

    print("Lap #" + str(lap))
    p.setPredator(bool(randint(0, 1)))
    p.notifyObservers()
