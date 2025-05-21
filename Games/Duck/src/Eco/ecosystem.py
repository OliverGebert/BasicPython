from random import choice  #, randint
from Eco.BirdFactory import createBird, BirdAttributes
from Eco.HumanFactory import createHuman, GadgetAttributes
from Eco.PredatorFactory import createPredator, PredatorAttributes
from Eco.habitant import Habitant


class Patch():

    patchDict = {
        "o": {
            "name" : "none",
            "char" : "o",
            "color" : "37m",
            "ground" : 0,
            "view" : 0
        },
        "f": {
            "name": "Forrest",
            "char": "F",
            "color": "32m", # green
            "ground" : 1,
            "view": 2
        },
        "w": {
            "name": "Water",
            "char": "W",
            "color": "34m", # blue
            "ground" : 1,
            "view": 8
        },
        "b": {
            "name": "Beach",
            "char": "B",
            "color": "33m", # yellow
            "ground" : 1,
            "view": 7
        }
    }
    patchTypes = list(patchDict.keys())  # Beach, Gras

    def __init__(self, type):
        self.patch = Patch.patchDict[type]
        self.habitant: Habitant = Habitant("e")

    def returnName(self):
        return self.patch["name"]

    def returnChar(self):
        return self.patch["char"]

    def returnColor(self):
        return self.patch["color"]

    def isHabitable(self):
        return False if self.patch["view"] == 0 else True

    def returnView(self):
        return self.patch["view"]

    def returnHabitantID(self):
        return self.habitant.returnHabitantID()

    def returnHabitantDescription(self):
        return self.habitant.returnDescription()

 
class Ecosystem():
    def __init__(self, y: int, x: int, ecolist):
        self.y = y # zeile
        self.x = x # spalte
        self.grid = []
        for _ in range(y):  # äußere Schleife: Zeile (vertikal)
            row = []
            for _ in range(x):  # innere Schleife: Spalte (horizontal)
                patch_type = choice(ecolist or "o")
                ecolist.remove(patch_type) if patch_type in ecolist else None
                row.append(Patch(patch_type))
            self.grid.append(row)

    def populateEcosystem(self, hList):
        # poulate patches in grid with habitants according to hList
        for y in range(len(self.grid)):
            zeile = []
            for x in range(len(self.grid[y])):
                if self.grid[y][x].isHabitable():
                    habitantType = choice(hList or "e")
                    hList.remove(habitantType) if habitantType in hList else None
                    match habitantType:
                        case "b":
                            hab = createBird(choice(BirdAttributes.birdList))
                        case "h":
                            hab = createHuman(choice(GadgetAttributes.gadgetList))
                        case "p":
                            hab = createPredator(choice(PredatorAttributes.predatorList))
                        case "e":
                            hab = Habitant("e")
                    self.grid[y][x].habitant = hab

    def plotEcosystem(self):
        report = []
        for y in range(len(self.grid)):
            info = []
            zeile = []
            for x in range(len(self.grid[y])):
                patchcolor = self.grid[y][x].returnColor()
                symbol = self.grid[y][x].returnHabitantID() or "="
                zeile.append("\033[" + patchcolor + symbol + "\033[0m")
                info.append(self.grid[y][x].returnName() + " " + self.grid[y][x].habitant.returnDescription() + ",")
            print(" ".join(zeile))
            report.append(" ".join(info))
            report.append("\n")
        print("".join(report))

    def lapEcosystem():
        pass

patchList = list("wwbbbbwfffff")  #define the nature of the patches on the ecosystem
habitantList = list("bbhbbpppp")    # define the habitants on the ecosystem

e = Ecosystem(3, 5, patchList)
e.plotEcosystem()
e.populateEcosystem(habitantList)
e.plotEcosystem()
