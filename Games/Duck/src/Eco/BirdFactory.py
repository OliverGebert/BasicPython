from Eco.bird import Duck, Gull, Swan


def createBird(type):
    match type:
        case "duck":
            bird = Duck()
        case "gull":
            bird = Gull()
        case "swan":
            bird = Swan()
    return bird
