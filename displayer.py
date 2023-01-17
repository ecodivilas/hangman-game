import pyfiglet as pfg
import os
import main as m

output = [
'''     _____
    | /    
    |/      
    |      
    |      
    |      
    |      
  __|__
''',
'''     _____
    | /   |
    |/    |
    |      
    |      
    |      
    |      
  __|__
''',
'''     _____
    | /   |
    |/    |
    |     |      
    |      
    |      
    |      
  __|__
''',
'''     _____
    | /   |
    |/    |
    |     |      
    |     O 
    |      
    |      
  __|__
''',
'''     _____
    | /   |
    |/    |
    |     |      
    |     O 
    |    /|\\ 
    |    / \\
  __|__
''',
'''"Success isn't just about what you accomplish in your life;
it's about what you inspire others to do."''',
'''The greatest glory in living lies not in never falling,
but in rising every time we fall.'''
]

def clear_screen():
    # Clear screen to avoid distraction
    os.system('cls||clear')
    # Use the FigletFont class to create a Beautiful Header
    print(pfg.figlet_format('H a n g m a n',
                            font="slant",
                            justify="left",
                            width=200
                            ))

def game_intro(lives, time_limit):
        # Intro to game
        print(f'''\nWelcome to Ely's: The Hang-er-man Game!\n 
Game Rules:
* Limit to {lives} wrong guess attempts before getting hangged
* Only {time_limit} seconds to guess the word to break the gallows
''')
        # Prompt if the player is Ready
        while True:
            game = input("Start Surviving? (y if YES, n if NO) : ")
            if game.strip() == "y":
                print("\nThe game is about to start!\nYou have ", end="")
                print(f"{time_limit} seconds to guess the hidden word.\n")
                break
            else:
                pass

# Print Fail Sketch
def display_failed_attempt(failed_attempts, lives):

    # Print if you runs out of attempt
    if failed_attempts == 5:
        print(f"{output[failed_attempts-1]}You are hanged!!!\n")
            
    # Print the remaining attempts
    elif failed_attempts > 0:
        rem_attempt = f"{str(lives - failed_attempts)} guesses remaining. "
        print(f"{output[failed_attempts-1]}\n{rem_attempt}", end="")

# Print the letter when the input was invalid
def invalid_input():
    print("\nInvalid input, try a letter.\n")

# Print when the letter was guessed
def letter_guessed():
    print("\nThe letter is guessed, try another letter.\n")

# Print when player gets the correct word
def print_correct(hidden_word):
    print("\You are perfectly CORRECT,", end="")
    print(f"the word was [==>  {hidden_word}  <==].")
    print("You are now safe and sound!\n")

# Print if the time lapsed
def game_over(): 
    # Clear screen
    clear_screen()
    print(f"Sorry, times up!\n{output[4]}")
    print("\nYou are hanged!!! Game Over!\n")
    print("Press any key to continue...", end="")

# Prompt the user to play again
def replay_prompt():
    print(f"{output[6]}\n") # Print lose quotes
    
    while True:
        print("\nDo you want to play ", end="")
        print("again? y for Yes, n for No) : ", end="")
        replay = input()
        if replay == "y":
            m.game()
        elif replay == "n":
            print("\nI admire your bravery, fella! ", end="")
            print("'Til our paths cross again. \n")
            break
        else:
            print("\nI need the right response, fella.\n")
            continue

def reveal_word(guessed_letters, hidden_word):
    # Reveal the word once the game was over
    print(f"The word {guessed_letters} was : {hidden_word}\n")
    