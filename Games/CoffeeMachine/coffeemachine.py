class CoffeeMachine:
    water = {"water": 250,
            "milk": 0,
            "coffee": 0,
            "sugar": 0,
            "cost": 50}

    latte = {"water": 50,
            "milk": 100,
            "coffee": 10,
            "sugar": 5,
            "cost": 250}

    coffee = {"water": 100,
            "milk": 0,
            "coffee": 20,
            "sugar": 0,
            "cost": 220}

    drinks = {"water": water,
            "latte": latte,
            "coffee": coffee}

    def __init__(self, water, milk, coffee, sugar):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.sugar = sugar

    def report(self):
        return f"\nwater: {self.water}\nmilk: {self.milk}\ncoffee: {self.coffee}\nsugar: {self.sugar}" 

    def optionen(self):
        optionen = []
        optionen.append("stop")
        optionen.append("report")
        for drink in self.drinks:
            optionen.append(drink)
        return optionen

    def makeDrink(self, drink):
        self.water -= self.drinks[drink]["water"] 
        self.milk -= self.drinks[drink]["milk"]
        self.coffee -= self.drinks[drink]["coffee"]
        self.sugar -= self.drinks[drink]["sugar"]
        return True

    def checkIngredientsSufficient(self, drink):
        """check that all ingredients are still sufficient to serve drink"""
        return int(self.water) >= int(self.drinks[drink]["water"]) and int(self.milk) >= int(self.drinks[drink]["milk"]) and int(self.coffee) >= int(self.drinks[drink]["coffee"]) and int(self.sugar) >= int(self.drinks[drink]["sugar"])

    def checkDrinkExists(self, drink):
        return drink in self.drinks 
    
