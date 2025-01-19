from duck import RealDuck, RubberDuck, WoodenDuck, FlyPropeller

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
