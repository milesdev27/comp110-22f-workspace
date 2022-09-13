"""Wordle!!!"""
__author__ = "730615836"


def contains_char(secret_word: str, guess: str) -> bool:  # search the secret word for a specific character
    """Generates a str value of either True or False."""
    assert len(guess) == 1
    found: bool = False
    a: int = 0
    while found is False and a < len(secret_word):
        if guess == secret_word[a]:
            found = True
        else:
            a += 1
    return found


def emojified(guess: str, secret: str) -> str:  # print out a string of boxes corresponding with letters
    """Generates a str of either green, yellow, or white boxes."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    output: str = ""
    a: int = 0
    while a < len(secret):
        if guess[a] == secret[a]:
            output += GREEN_BOX
        else:
            if contains_char(secret, guess[a]):
                output += YELLOW_BOX
            else:
                output += WHITE_BOX
        a += 1
    return output


def input_guess(expected_len: int) -> str:
    """Generates an int value for the word length."""
    guess: str = input(f"Enter a {expected_len} character word: ")
    while len(guess) != expected_len:  # wrong number of characters in guess
        guess = input(f"That wasn't {expected_len} chars! Try again: ")
    return guess


def main() -> None:  # part of program being run
    """The entrypoint of the program and main game loop."""
    i: int = 1  # turn number
    secret_word: str = "codes"
    while i <= 6:
        print(f"=== Turn {i}/6 ===")
        guess: str = (input_guess(len(secret_word)))
        print(emojified(guess, secret_word))
        if guess == secret_word:  # guessed word
            print(f"You won in {i}/6 turns!")
            i = 7
        else:
            i += 1
    if i == 7 and guess != secret_word:  # didn't guess word
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()