from Eco.human import Human, Foto, Gun, Bag


def createHuman(type):
    raw = Human()
    match type:
        case "foto":
            human = Foto(raw)
        case "gun":
            human = Gun(raw)
        case "bag":
            human = Bag(raw)
    return human
