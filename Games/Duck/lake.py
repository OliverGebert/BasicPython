from interfaces import ISubject


class Lake(ISubject):

    def __init__(self, cap, pred):
        self.capacity = int(cap)
        self.habitantlist = []
        self.danger = 0

    def registerObserver(self, habitant, danger):
        if (len(self.habitantlist) < self.capacity):
            self.habitantlist.append(habitant)
            self.danger += danger

    def removeObserver(self, habitant):
        # missing implementation of removing habitants from lake,
        # also test_removeObserver not implemented
        pass

    def notifyObservers(self):
        print("Danger status: " + str(self.danger))
        print("predator at lake: " + str(self.hasPredator()))

        for h in self.habitantlist:
            h.update(self.danger)

    def count(self):
        return len(self.habitantlist)

    def hasPredator(self):
        predator = False
        for habitant in self.habitantlist:
            if ("gun" in habitant.getDescription()) or ("predator" in habitant.getDescription()):
                predator = True

        return predator

    def setCapacity(self, cap):
        self.capacity = cap
