# interactive blackjack game

import random as rand

stackIDs = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "B", "D", "K", "A"]
decks = 8  # number od decks in shoe
# create a shoe of cards
shoe = {"2": decks,
        "3": decks,
        "4": decks,
        "5": decks,
        "6": decks,
        "7": decks,
        "8": decks,
        "9": decks,
        "10": decks,
        "B": decks,
        "D": decks,
        "K": decks,
        "A": decks
        }


def dealCard():
    """return a random card from the shoe, which still exists"""
    global shoe
    global stackIDs
    # take one new card from the stack
    card = rand.choice(stackIDs)
    # loop until card is selected which still is in shoe
    shoe[card] -= 1
    if shoe[card] == 0:
        stackIDs.remove(card)    # remove card from stackIDs
        # debug: print(f"{card} from shoe removed")
    return card


def countShoe():
    """return number of cards in shoe"""
    global shoe
    return sum(shoe.values())


def evalHand(hand):
    """returns the value of a hand"""
    handValue = 0
    # iterate elements in hand and add up the values
    for element in hand:
        match element:
            case "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" | "10":
                handValue += int(element)
            case "B" | "D" | "K":
                handValue += 10
            case "A":
                handValue += 11

    # check if hand is to  high and ass can be reduced to value of One
    if handValue > 21 and "A" in hand:
        handValue -= 10
    return handValue


def hasBlackJack(hand):
    """returns True if hand has a blackjack"""
    if (len(hand) == 2) and (evalHand(hand) == 21):
        return True
    else:
        return False


def displayCards():
    """display the cards of the player and the dealer"""
    print(f"\nDealer cards: {handDealer} with a value of: {
          evalHand(handDealer)}")
    print(f"Player cards: {handPlayer} with a value of: {
          evalHand(handPlayer)}")


def displayCash():
    """display the cash of the player and the dealer"""
    print(f"Dealer has {cashDealer} cashes")
    print(f"Player has {cashPlayer} cashes")
    print(f"Pot has {cashPot} cashes")


def displayResult(handPlayer, handDealer):
    """display the result of the game"""
    global cashDealer
    global cashPlayer
    global cashPot
    global einsatz
    # bet gies to the dealer for distribution in case Player has won
    cashDealer += cashPot
    cashPot = 0

    if evalHand(handPlayer) > 21:
        print(f"\n--> Player bust")
    elif evalHand(handDealer) > 21:
        print(f"\n--> Dealer lost")
        cashPlayer += einsatz * 2
        cashDealer -= einsatz * 2
    elif evalHand(handPlayer) < evalHand(handDealer):
        if hasBlackJack(handDealer):
            print(f"\n--> Dealer won - Dealer has blackjack")
        else:
            print(f"\n--> Dealer won")
    elif evalHand(handPlayer) > evalHand(handDealer):
        if hasBlackJack(handPlayer):
            print(f"\n--> Player won - Player has BlackJack")
            cashPlayer += einsatz * 3
            cashDealer -= einsatz * 3
        else:
            print(f"\n--> Player won")
            cashPlayer += einsatz * 2
            cashDealer -= einsatz * 2
    else:
        if hasBlackJack(handPlayer) and hasBlackJack(handDealer):
            # both having BlackJack, both get back their bet
            print(f"\n--> draw - Both have BlackJack")
            cashPlayer += einsatz
            cashDealer -= einsatz
        elif hasBlackJack(handPlayer):
            # player has BlackJack, player gets back 3:2
            print(f"\n--> Player won - Player has BlackJack")
            cashPlayer += einsatz * 3
            cashDealer -= einsatz * 3
        elif hasBlackJack(handDealer):
            # dealer has BlackJack, dealer gets back 2:1
            print(f"\n--> Dealer won - Dealer has BlackJack")
        else:
            # both are equal with no BlackJack, player gets back 1:1
            print(f"\n--> draw")
            cashPlayer += einsatz
            cashDealer -= einsatz


# initialize game
print("***** Welcome to blackjack *****")
einsatz = 100
cashDealer = 5 * einsatz
cashPlayer = 5 * einsatz
cashPot = 0

""" debug: test cases for correct displayResults
displayResult(["A","D"], ["A", "B"])             # both have 21, draw - both have BlackJack
displayResult(["A","5", "5"], ["A", "B"])        # both have 21, Dealer won - Dealer has BlackJack
displayResult(["D", "A"],["6", "A", "4"])        # both have 21, Player won - Player has BlackJack
displayResult(["D", "A"],["9", "A", "8", "2"])   # player has 21 - Player won - Player has BJ
displayResult(["4","9"],["A", "10"])             # dealer has 21 - Dealer won - Dealer has BJ
displayResult(["D", "K"],["6", "B", "4"])        # both have 20 - draw
displayResult(["5", "4", "B"],["K", "8"])        # player won
displayResult(["7", "2", "2", "6"],["K", "D"])   # Dealer won
displayResult(["D", "8", "5"],["3", "K", "6"])   # Player lost - bust
displayResult(["9", "B"],["7", "B", "D"])        # Dealer lost - bust
"""

# start game
while cashDealer >= 100 and cashPlayer >= 100 and countShoe() > 15:

    # start round
    handDealer = []  # no cards in hand
    handPlayer = []  # no cards in hand
    cashPlayer -= einsatz    # pay einsatz
    cashDealer -= einsatz    # pay einsatz
    cashPot += 2 * einsatz     # add einsatz to round cash
    playerStop = False    # set default to continue

    print("\n----- new round -----")
    handDealer.append(dealCard())
    handPlayer.append(dealCard())
    handPlayer.append(dealCard())
    displayCash()
    displayCards()

    # player plays
    while (evalHand(handPlayer) < 21) and (playerStop is False):
        # ask the player if he wants to take another card
        if input("pull another card? (y/n): ") == "y":
            handPlayer.append(dealCard())
            displayCards()
        else:
            playerStop = True

    # dealer plays
    while (evalHand(handPlayer) < 22) and (evalHand(handDealer) < 17):
        handDealer.append(dealCard())
        displayCards()

    # show end result
    displayResult(handPlayer, handDealer)

print(f"\n***** Game over *****")
displayCash()
print(f"remaining cards in shoe: {countShoe()}")
# debug: print(f"shoe: {shoe}"))
