from predator import Wolf, Fox


def createPredator(lake, type):
    match type:
        case "wolf":
            predator = Wolf(lake)
        case "fox":
            predator = Fox(lake)
    return predator
