"""EX02 - One-Shot Wordle."""

__author__ = "730706009"


# Define the secret word for the Wordle game
secret: str = "python"


def is_valid_guess(guess: str) -> bool:
    """Check if a guess is valid (6 letters)."""
    return len(guess) == 6 and guess.isalpha()


def is_correct_guess(guess: str) -> bool:
    """Check if a guess is correct."""
    return guess == secret


# Define Unicode box characters for displaying Wordle results
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


# Initialize an empty string to build the Wordle squares display
wordleSquares: str = ""


# Main game loop
guess: str = input("What is your 6-letter guess? ")

while not is_valid_guess(guess):
    print("That was not 6 letters! Try again: ")
    

# Compare each letter of the guess to the corresponding letter in the secret word using a for loop
for i in range(len(guess)):
    if guess[i] == secret[i]:
        # If the letter is correct and in the correct position, add a green box
        wordleSquares += GREEN_BOX
    elif guess[i] in secret:
        # If the letter is correct but in the wrong position, add a yellow box
        wordleSquares += YELLOW_BOX
    else:
        # If the letter is incorrect, add a white box
        wordleSquares += WHITE_BOX


# Display the Wordle squares
print(wordleSquares)

if is_correct_guess(guess):
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")