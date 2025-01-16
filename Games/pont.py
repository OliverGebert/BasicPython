from duck import Duck, RubberDuck

ducks = []
ducks.append(Duck("green", "water"))
ducks.append(RubberDuck("pink", "rubber"))
ducks.append(Duck("brown", "water"))

for d in ducks:
    print(d.draw())
    print(d.quak())
    print(d.fly())
