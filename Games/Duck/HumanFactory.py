from human import Human, Foto, Gun, Bag


def createHuman(lake, type):
    raw = Human(lake)
    match type:
        case "foto":
            human = Foto(lake, raw)
        case "gun":
            human = Gun(lake, raw)
        case "bag":
            human = Bag(lake, raw)
    return human
