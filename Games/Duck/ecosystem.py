from random import choice, randint
from duck import RealDuck, DuckAttributes
from pont import Pont
from human import Human, Foto, Gun

systemLaps = 10
pontCapacity = 6
p = Pont(pontCapacity, False)

for lap in range(systemLaps):

    if (p.count() < pontCapacity - 3):
        # problem: even if no space in pont left, object is instanciated
        color = choice(DuckAttributes.colorList)
        type = choice(DuckAttributes.typeList)
        d = RealDuck(color, type, p)

    print("Lap #" + str(lap))
    p.setPredator(bool(randint(0, 1)))
    p.notifyObservers()

h = Human(p)
h_f = Foto(p, h)
h_f_g = Gun(p, h_f)
p.notifyObservers()
