# Jesus Robles
# 1/27/2020
# Gamecenter.py

# This program displays a user to the user to play from various game options: hangman or brickbreaker

import hangman
import brickbreaker

def print_menu():
    print("Which game would you like to play?")
    print("Enter the number associated with the following options:")
    print("1: Hangman")
    print("2: Brickbreaker")
    print("3: quit program :(")

def get_user_choice():
    """ Promots user to enter choice from menu until a valid choice has been entered
        - KeyboardInterrupt turns choice to 3 which is equivalent to quit
    """

    choice = None

    while(not choice):

        try:
            choice = int(input("Give me the number associated with your choice: "))
            if not(0 < choice < 4):
                raise(ValueError)

            return choice

        except ValueError:
            print("The value entered was not valid")
            choice = None

        except KeyboardInterrupt:
            print("Okay, goodbye!")
            return 3


def main():

    choice = None  # Stores user input

    print("Hello! Welcome to Gamecenter!")

    while (not choice == 3):

        print_menu()
        choice = get_user_choice()

        if(choice == 1):
            hangman.main()
            print("Hope you enjoyed that game!\n\n")

        if(choice == 2):
            print("A graphics window has opened!")
            brickbreaker.main()
            print("Hope you enjoyes that game!\n\n")

        if(choice == 3):
            print("Thank you for playing!")


main()
