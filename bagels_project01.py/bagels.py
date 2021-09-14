"""
Bagles, a deductive logic game, where you guess a secret three-digit number based on glues. The game offers one of the follogin hints in response to your guess: "Pico" when you guess has a correct digit in the wrong place, "Fermi" when you guess has a correct digit in the correct place, and "Bagels" if your guess has no correct digits. You have 10 tries to guess the secret number.
"""
import random


def guessed_correct(secret_number, user_guess):
    """
    Comparing two strings to check whether they have any characters in common. 
    """
   
    if user_guess == secret_number:
        return True
    else:
        for i in user_guess:
            if i in secret_number:
                if secret_number.find(i) == user_guess.find(i):
                    print("Fermi")
                else:
                    print("Pico")



def secret_number():
    """
    Guessing a secret number using random module.
    """
    
    return random.randint(100, 999)


def game_info():
    """
    Telling the user about the rules and clues about the game.
    """
    print("Bagels, a deductive logic game.")
    print("\nI am thinking of a 3-digit number. Try to guess what it is.")
    print("Here are some clues: ")
    print("When i say:        That means:")
    print("    Pico           One digit is correct but in the wrong position.")
    print("    Fermi          One digit is correct and in the right position.")
    print("    Bagels         No digit is correct.")
    print("I have thought up a number.")
    print("You have 10 guesses to get it.")


def main():
    
    game_info()
    secret_num = str(secret_number())

    guess_chance = 10

    while guess_chance != 0:
        print("You have " + str(guess_chance) + " guesses remaining.")
        user_guess = input("Enter your guess: ")
        result = guessed_correct(secret_num, guess_chance) 
       

