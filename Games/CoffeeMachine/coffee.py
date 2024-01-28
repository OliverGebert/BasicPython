from coffeemachine import CoffeeMachine
from purse import Purse

coffe_machine = CoffeeMachine(2000, 200, 250, 250)
purse = Purse(3, 4, 5, 10)      # your money to pay drinks
money_machine = Purse(10, 20, 20, 20)   # money which trhe machine has earned
machine_stock = Purse(0,0,0,0)  # money which was entered into the machine for payment
# print(f"+++ precondition: {coffe_machine.report()}\n")
selection = False

while not selection:
    select = input(f"\nPlease select drink: ")
    if coffe_machine.checkDrinkExists(select):
        if coffe_machine.checkIngredientsSufficient(select):
            print(f"the drink: {select} costs {coffe_machine.drinks[select]['cost']}")
            # collect coins until enough coins are entered
            while int(coffe_machine.drinks[select]["cost"]) > machine_stock.total_value(): 
                print(f"\nyou have {purse.total_value()} cent. You have following coins: {purse.showCoins()}")
                print(f"There is {machine_stock.total_value()} in the machine. with following coins: {machine_stock.showCoins()}")
                # only use coins which are in purse
                coins = input("please enter coins (euro,funfzig,zwanzig,zehn): ").split(',')
                if purse.checkCoins(coins):
                    purse.useCoins(coins)           # remove coins from purse
                    machine_stock.addCoins(coins)   # add coins to machine stock
                else: 
                    print("coins not available in purse")

            payment = machine_stock.provideCoinsForValue(coffe_machine.drinks[select]["cost"])
            print(f"folgende Münzen werden zur Zahlung genutzt: {payment}")
            machine_stock.useCoins(payment)
            money_machine.addCoins(payment)
            coffe_machine.makeDrink(select)
            
            print(f"here is your drink: {select}")
            print(f"\nyou have {purse.total_value()} cent. You have following coins: {purse.showCoins()}")
            print(f"There is {machine_stock.total_value()} in the machine. with following coins: {machine_stock.showCoins()}")
        else:
            print(f"not enough ingredients\n{coffe_machine.report()}")
    else:
        if select == "stop":
            change = machine_stock.showCoins()
            print(f"you get {machine_stock.total_value()} cent return with following coins: {change}")
            purse.addCoins(change)
            machine_stock.useCoins(change)
            selection = True 
        elif select == "report":
            print(f"\n+++ machine report: \n{coffe_machine.report()}")
            print(f"the Machine has {money_machine.total_value()} cent. with following coins: {money_machine.showCoins()}") 
        else:
            print(f"bitte valide eingabe vornehmen: {coffe_machine.optionen()}")
            
print(f"\n+++ machine report: \n{coffe_machine.report()}")
print(f"the Machine has {money_machine.total_value()} cent. with following coins: {money_machine.showCoins()}") 
print(f"You have {purse.total_value()} cent in your purse with following coins: {purse.showCoins()}")