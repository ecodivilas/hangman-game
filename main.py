# Hangman

# Useful imports
from random import choice
from time import sleep

# Import from external file
from timer import RepeatableTimer
import displayer as dp
import words as w

# Remaining lives
lives = 5
# Timer limit set to 30 sec                  
time_limit = 30            

# Game callable function program starts here:
def game():

    # This clear the screen
    dp.clear_screen()
    dp.game_intro(lives, time_limit)

    # Selects a word to be guess
    already_guessed = []
    hidden_word = choice(w.words)
    unguessed_letters = hidden_word
    guessed_letters = '_' * len(hidden_word)
    incorrect_letters = ""
    is_letter_guessed = False
    is_invalid_input = False
    is_failed = False

    # Initialize new instance of a Timer
    game_timer = RepeatableTimer(time_limit, dp.game_over)
    sleep(2)
    # Game timer starts
    game_timer.start()
    failed_attempts = 0

    while True:
        # Clear the screen
        dp.clear_screen()

        # Check if word was guessed already
        if hidden_word == guessed_letters:
            dp.print_correct(hidden_word)
    
            # Cancel the timer
            game_timer.cancel()
            break

        elif failed_attempts == 5:
            # Display Fail Sketch
            dp.display_failed_attempt(failed_attempts, lives)
            # Reveal the word once the game was over
            dp.reveal_word(guessed_letters, hidden_word)
            game_timer.cancel()
            break
        
        if game_timer.is_alive():
            pass
        else:
            break
    
        # Game status displays Remaining Time, Missing word
        print(f"Remaining Time: {game_timer.get_remaining_time()} sec.")
        print(f"Missing word : {guessed_letters}")
        print(f"Incorrect letters : {incorrect_letters}")

        # Check if the input is valid
        if is_invalid_input:
            dp.invalid_input()
            # Reset the input status
            is_invalid_input = False
            
        if is_letter_guessed:
            dp.letter_guessed()
            # Reset the input status
            is_letter_guessed = False

        # Display Hangman Illustration
        dp.display_failed_attempt(failed_attempts, lives)

        if is_failed:
            print("Wrong guess. ", end="")

        # Prompt the player to guess the hidden word
        try :
            guess = input("\nEnter your guess w/ letters : ")
            print()
        except OSError as e :
            pass

        else:
            # Validation if guess letter length is 0 or more than 1 or number 
            if len(guess.strip()) == 1 and guess.isalpha():
                
                # Check if guess letter have in word string
                if guess in unguessed_letters:
                    already_guessed.extend([guess]) # List
                    for index, remaining_letters in enumerate(unguessed_letters):
                        if remaining_letters == guess:
                            # Refresh unguessed letters
                            unguessed_letters = unguessed_letters[:index] + "_" \
                            + unguessed_letters[index + 1:] # word being guessing
                            # Refresh guessed letters
                            guessed_letters = guessed_letters[:index]\
                            + guess + guessed_letters[index + 1:]
                            is_failed = False
        
                # Check if letter was guessed
                elif guess in incorrect_letters:
                    is_letter_guessed = True
                    is_failed = True
                elif guess in already_guessed:
                    is_letter_guessed = True
                    is_failed = False
                else:
                    # Store all footprints of guess letters
                    incorrect_letters += (", " + guess) \
                    if len(incorrect_letters) >= 1 else guess 
                    # Wrong guessing increases failed_attempts
                    failed_attempts += 1
                    is_failed = True
                is_invalid_input = False
            else:
                is_invalid_input = True
                        
# End of the game loop

# Main Game Flow
if __name__ == "__main__":
    # Call the game program
    game()

    # Call a prompt that ask the player to play again
    dp.replay_prompt()