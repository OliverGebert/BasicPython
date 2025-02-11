from bird import Duck, Gull, Swan


def createBird(lake, type):
    match type:
        case "duck":
            bird = Duck(lake)
        case "gull":
            bird = Gull(lake)
        case "swan":
            bird = Swan(lake)
    return bird
