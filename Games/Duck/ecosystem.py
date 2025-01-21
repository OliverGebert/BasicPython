from random import choice
from duck import RealDuck, DuckAttributes
from pont import Pont

systemLaps = 10
pontCapacity = 3
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

"""
ducks = []
ducks.append(RealDuck("green", "water"))
ducks.append(RubberDuck("pink", "rubber"))
ducks.append(WoodenDuck("brown", "wooden"))

for d in ducks:
    print("----------")
    print(d.draw())
    print(d.performQuack())
    print(d.performFly())

for d in ducks:
    if "wooden" in d.draw():
        d.setFlyBehavior(FlyPropeller())
    print("----------")
    print(d.draw())
    print(d.performQuack())
    print(d.performFly())
"""
