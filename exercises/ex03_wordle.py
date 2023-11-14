"""EX03 - Structured Wordle."""

__author__ = "730706009"


def contains_char(search_str: str, single_char: str) -> bool:
    """Check if the character is contained in the word."""
    assert len(single_char) == 1  # Ensure char is a single character
    index = 0
    while index < len(search_str):
        if search_str[index] == single_char:
            return True
        index += 1
    return False


# Define Unicode box characters for displaying Wordle results
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret_word: str) -> str:
    """Generate an emoji representation of the guess compared to the secret."""
    assert len(guess) == len(secret_word)  # Ensure secret and guess have the same length
    result = ""
    index = 0
    while index < len(secret_word):
        if guess[index] == secret_word[index]:
            result += GREEN_BOX
        elif contains_char(secret_word, guess[index]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        index += 1
    return result


def input_guess(expected_length: int) -> str:
    """Prompt the user for a guess of the expected length."""
    while True:
        guess = input(f"Enter a {expected_length} character word: ")
        if len(guess) == expected_length:
            return guess
        else:
            print(f"That wasn't {str(expected_length)} chars! Try again:")


def main() -> None: 
    """The entry point of the program and main game loop."""
    secret_word = "codes"  # Replace with your secret word
    max_attempts = 6
    attempts = 0
    
    print(f"=== Turn {attempts + 1}/{max_attempts} ===")
    
    while attempts < max_attempts:
        guess = input_guess(len(secret_word))
        result = emojified(secret_word, guess)
        print(result)
        if result == GREEN_BOX * len(secret_word):
            print(f"You won in {attempts + 1}/{max_attempts} turns!")
            break
        else:
            attempts += 1
            remaining_attempts = max_attempts - attempts
            if remaining_attempts > 0:
                print(f"=== Turn {attempts + 1}/{max_attempts} ===")
                print(f"Remaining attempts: {remaining_attempts}")
            else:
                print(f"X/{max_attempts} - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()
