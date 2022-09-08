"""EX02 One-Shot Wordle"""
__author__ = 730615836

secret_word: str = ("python")
guess: str = input(f"What is your {len(secret_word)}-letter guess? ")

#boxes
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
output: str = ""

while len(guess) != len(secret_word):
    guess = input(f"That was not {len(secret_word)} letters! Try again: ")

#incorrect guess
if guess != secret_word:
    a: int = 0 #index of secret_word
    while a < len(secret_word): #checking word for direct matches
        if guess[a] == secret_word[a]:
            output += GREEN_BOX
        elif guess[a] != secret_word[a]:
            b: int = 0 #index of secret_word if !=
            found: bool = False
            while found is False and len(secret_word) > b: #checking word for letter        
                if guess[a] == secret_word[b]:
                    found = True
                else:
                    b += 1
            if found is True: #found match in word
                output += YELLOW_BOX
            else: #no match found
                output += WHITE_BOX
        a += 1
    print(output) #final word
    print("Not quite. Play again soon!")

#correct guess
else:
    a = int(0)
    while a < len(secret_word):
        if guess[a] == secret_word[a]:
            output = output + GREEN_BOX
        a += 1
    print(output)
    print("Whoo! You got it!")
