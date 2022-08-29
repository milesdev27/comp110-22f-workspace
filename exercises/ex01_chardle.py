"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730615836"

word: str = input("Enter a 5-character word: ")
if len(word) != 5:
    print("Word must contain 5 characters")
    exit()
letter: str = input("Enter a single character: ")
if len(letter) != 1:
    print("Character must be a single character")
    exit()
instance = int(0)
print("Searching for " + letter + " in " + word + "")
if letter == word[0]:
    print(letter + " found at index 0")
    instance = instance + 1
if letter == word[1]:
    print(letter + " found at index 1")
    instance = instance + 1
if letter == word[2]:
    print(letter + " found at index 2")
    instance = instance + 1
if letter == word[3]:
    print(letter + " found at index 3")
    instance = instance + 1
if letter == word[4]:
    print(letter + " found at index 4")
    instance = instance + 1
if instance == 1:
    print("1 instance of " + letter + " found in " + word)
if instance == 0: 
    print("No instances of " + letter + " found in " + word)
if instance > 1: 
    print(str(instance) + " instances of " + letter + " found in " + word)