import random

import hang

hangsequence = hang.hangsequence
chosen_word_list = list(hang.word_list[random.randint(0,
                                                      len(hang.word_list) -
                                                      1)])
guess_word_list = list("_" * len(chosen_word_list))
hangman = len(hangsequence) - 1
choices = {}

while (guess_word_list != chosen_word_list) and hangman > 0:
    guess_word = "".join(guess_word_list)
    print(
        f"search: {guess_word}  -  offene Leben: {hangman}\n{choices}\n{hangsequence[hangman]}\n"
    )
    guess = input("Guess a letter: ")
    if guess not in choices:  # otherwise while loop for next guess
        if guess in chosen_word_list:  # guess is new and in chosen_word_list
            for i in range(len(chosen_word_list)):
                if guess == chosen_word_list[i]:
                    guess_word_list[i] = guess  # substuitute _ with guess
                    if guess not in choices:
                        choices[guess] = 1  # initiate choices dict
                    else:
                        choices[guess] = choices[
                            guess] + 1  # add 1 to choices dict
        else:  # guess is new and not in chosen_word_list
            hangman += -1
            choices[guess] = 0

chosen_word = "".join(chosen_word_list)
guess_word = "".join(guess_word_list)
print(
    f"search: {guess_word}  -  offene Leben: {hangman}\n{choices}\n{hangsequence[hangman]}\n"
)
if hangman == 0:
    print("you lost \n")
    print(f"The word was {chosen_word}")
else:
    print("You guessed the word!\n")
