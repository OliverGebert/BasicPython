import random as rand
from os import system
from pathlib import Path
from time import sleep


def importAccountList(fileName):
    """imports a list of accounts into a list of lists"""
    accountList = []
    with open (fileName, 'r') as file:
        lines = file.read().splitlines()
    for line in lines:
        item = line.split(';')
        accountList.append(item)
    return accountList

fileName = "AccountList.csv"
fullPath = Path(__file__).parent / fileName
print(fullPath)
liste = importAccountList(fullPath)

counter = 0             # set game counter to zero
nextRound =  True       # start game 
base = rand.choice(liste)   # select first entry for comparison

while nextRound:
    challenge = rand.choice(liste)  # select second entry for comparison
    while challenge == base:
        challenge = rand.choice(liste)
    if int(base[1]) > int(challenge[1]):
        answer = "A"
    elif int(base[1]) < int(challenge[1]):
        answer = "B"
    else:
        answer = "X"
    sleep(2)
    system('clear')
    print("\n***** next round *****\n")
    print(f"Celebrity A: {base[0]} is a {base[2]}")
    print(f"Celebrity B: {challenge[0]} is a {challenge[2]}")
    choice = input("Which one has more followers: ").upper()

    print(f"\n{base[0]} has {base[1]} followers")
    print(f"{challenge[0]} has {challenge[1]} followers")
    
    if choice == answer or answer == "X":
        counter += 1
        if answer == "B":
            base = challenge    # new base for next round
        print("you are correct")
    else:
        nextRound = False
        print("you are wrong")

print(f"\n***** Game ends, you earned {counter} points")