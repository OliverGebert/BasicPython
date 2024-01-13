import random

choice = ["R", "P", "S", "L", "S"]
longChoice = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

lineR = ["0", "-1", "1", "1", "-1"]
lineP = ["1", "0", "-1", "-1", "1"]
lineS = ["-1", "1", "0", "1", "-1"]
lineL = ["-1", "1", "-1", "0", "1"]
lineS = ["1", "-1", "1", "-1", "0"]
matrix = [lineR, lineP, lineS, lineL, lineS]

print("the Game is Rock Paper Scissors Lizard Spock")
userChoice = input("As user, please choose (R,P,S,L,S): ").upper()
computerChoice = choice[random.randint(0,4)]
print(f"User    : {longChoice[choice.index(userChoice)]}")
print(f"Computer: {longChoice[choice.index(computerChoice)]}\n")

if userChoice in choice:
    if matrix[choice.index(userChoice)][choice.index(computerChoice)] == "1":
        print("You win!")
    elif matrix[choice.index(userChoice)][choice.index(computerChoice)] == "-1":
        print("You lose!")
    else:
        print("Tie!")
else:
    print(f"Please only enter: {choice}")