class Duck:

    def __init__(self, color, type):
        self.color = str(color)
        self.type = str(type)

    def draw(self):
        return "Duck with color " + self.color + "/nDuck from type " + self.type

    def quak(self):
        return "quaaak"

    def fly(self):
        return "I feel so light"


class RubberDuck(Duck):

    pass


class WoodenDuck(Duck):

    pass
