# Jesus Robles
# 1/5/2021
# Hangman Game 

# This program will simulate Hangman by allowing the user to play the game generated

# Overall good improvements, nice to see it much more organized. I aggree with CC's
# 3 sauggestions to use more docstrings.

from random import randrange

MAX_LETTER = 26

# TODO: Write Test Functions
# KWD: Maybe add an option to something that allows you to guess the phrase by typing it


# KWD Return sayings, rather than writing to a variable in outer namespace.
def read_file(fileName):
    '''opens the file and saves each line into an list of strings (sayings) '''
    sayings = []

    with open(fileName, "r") as infile:
        i = 0
        while(1):
            sayings.append(infile.readline())

            if(sayings[i] == ""):
                break

            i += 1

    return sayings

# KWD Good iformational control here pass in, pass out.
def choose_random_saying(sayings):

    chosenSaying = randrange(0, len(sayings)-1)
    answer = sayings[chosenSaying]

    return answer

def print_welcome():

    print("\nWelcome. Get ready to play hangman. This should be interesting. How is your guessing game?\n")
    print("Instructions: ")
    print(" - You will be prompted to enter letters you believe make up the saying")
    print(" - Enter a letter and see how far you can get")
    print(" - Guess the entire line correctly before the man is hung. Choose wisely.\n")
    print("Goodluck!\n")

def print_game(answer, alphaSelected):
    ''' This function prints underscores for letters not yet selected by user and prints the rest as is '''
    for char in answer:

        if(char.isalpha() == True and alphaSelected[ord(char)-ord('a')] == 0):
            print('_', end='')
        else:
            print(char, end='')

# KWD: Good, getting all that hangman stuff out is nice, isn't it? YESSSS!
def print_man(numChances):
    ''' This function prints a hangman figure read in from a file based on number of chances left '''

    # Maps the number of chances left to the first line of the figure in the file 
    # The number 16 represents how many lines long each figure is in the file 
    if(numChances < 0):
        startIndex = numChances + 2
        endIndex = startIndex + 16
    else:
        startIndex = ((numChances+1)*16) + 1
        endIndex = startIndex + 16

    # Open file and print figure according to mapped line number in file
    with open("HangmanFigure.txt", 'r') as figfile:

        i = 1
        while(1):
            temp = figfile.readline()
            if(i >= startIndex and i < endIndex):
                print(temp, end='')
            i += 1
            if(i > endIndex):
                break
 
def get_user_guess():

    ''' Gets guess of character from user
        - Only accepts characters
        - Is flexible to accept strings but only returns first entered
        - Repeats until a valid choice has been entered
    '''

    # Prompt user to enter a guess until a valid choice is selected
    valid = False
    while (not valid):

        try:
            guess = str(input('Enter the letter you believe is in the saying: '))
            if(guess[0].isalpha() == True):

                guess = guess.lower()
                valid = True
        except KeyboardInterrupt:
            print("\nWow... that difficult?")
            return None

        else:
            print("The value entered was not a valid character in the alphabet. Please try again.")

    return guess[0]

def record_user_selection(alphaSelected, choice):
    # uses ascii value of letter to record in according index representing alphabet
    alphaSelected[ord(choice)- ord('a')] = 1


def check_correct_answer(answer, alphaSelected):
    ''' Iterates through answer to see if all characters in it have been selected by the user
        - Returns boolean
    '''

    # returns whether all characters in answer have been selected by user
    for char in answer:

        guessedAnswer = True
        if(char.isalpha() == True and alphaSelected[ord(char)-ord('a')] == 0):
            return False

    return guessedAnswer

def print_end_game(guessedAnswer):
    if(guessedAnswer):
        print("Congratulations! You got the answer!")

    else:
        print("Sorry, you were not able to guess the answer :(")

    print("Thank you for playing!")


def main():

    # Initialize Variables 
    fileName = "SayingsFile.txt" #Hardcoded name of file/ could be user input later
    alphaSelected = [0 for i in range(MAX_LETTER)]              # records letters selected by user
    numChances = 6

    # call to funtion to read sayings from file and choose random one for game
    sayings = read_file(fileName)
    answer = choose_random_saying(sayings)

    # Initial blank game shown to user 
    print_welcome()
    print_man(numChances)
    print_game(answer, alphaSelected)

    #WHILE loop that runs the program flow until the game is over
    guessedAnswer = False
    while(not guessedAnswer and numChances >= 0):

        guess = get_user_guess()

        #Handles condition if user used CTRL-C to exit game
        if(guess == None):
            print_man(-1)
            break

        record_user_selection(alphaSelected, guess)

        print("\n\n\n")                 # TODO: Delete this line and improve

        # Check if letter is in the answer
        if(guess in answer):
            print(f"The letter you entered, {guess}, was found in the clue!")
            guessedAnswer = check_correct_answer(answer, alphaSelected)

        else:
            print(f"The letter you entered, {guess}, was not found in the clue :(")
            numChances -= 1

        print_man(numChances)
        print_game(answer, alphaSelected)


    print("Answer: " + answer)

    print_end_game(guessedAnswer)

    return 0


if __name__ == "__main__":
    main()
