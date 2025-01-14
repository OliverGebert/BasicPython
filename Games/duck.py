class Duck:

    def __init__(self, color, type):
        self.color = str(color)
        self.type = str(type)

    def draw(self):
        return "Duck with color " + self.color + "/nDuck from type " + self.type

class RubberDuck(Duck):

    pass
