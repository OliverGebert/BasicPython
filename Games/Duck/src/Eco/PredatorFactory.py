from Eco.predator import Wolf, Fox


def createPredator(type):
    match type:
        case "wolf":
            predator = Wolf()
        case "fox":
            predator = Fox()
    return predator
