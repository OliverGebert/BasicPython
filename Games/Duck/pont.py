from duck import RealDuck, RubberDuck, WoodenDuck

ducks = []
ducks.append(RealDuck("green", "water"))
ducks.append(RubberDuck("pink", "rubber"))
ducks.append(WoodenDuck("brown", "wooden"))

for d in ducks:
    print("----------")
    print(d.draw())
    print(d.performQuack())
    print(d.performFly())
