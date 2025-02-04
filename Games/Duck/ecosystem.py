from random import choice, randint
from duck import RealDuck, DuckAttributes
from pont import Pont
from human import Human

systemLaps = 10
pontCapacity = 5
p = Pont(pontCapacity, False)

for lap in range(systemLaps):

    if (p.count() < pontCapacity - 1):
        color = choice(DuckAttributes.colorList)
        type = choice(DuckAttributes.typeList)
        d = RealDuck(color, type, p)

    print("Lap #" + str(lap))
    p.setPredator(bool(randint(0, 1)))
    p.notifyObservers()

h = Human(p)
p.notifyObservers()
