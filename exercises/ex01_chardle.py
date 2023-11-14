"""EX01 - Chardle - A cute step toward World."""

__author__ = "730706009"

# Input for the word
word = str(input("Enter a 5-character word: "))
if len(word) != 5:
    print("Error: Word must contain 5 characters ")
    exit()
letter = str(input("Enter a single character: "))
if len(letter) != 1:
    print("Error: enter only one character ")
    exit()

# Show what user is looking for
print("Searching for " + letter + " in " + word)
number = 0

if letter in word:
    for i in range(len(word)):
        if word[i] == letter:
            print(letter + " found at index " + str(i))
            number = number + 1
    if number > 1:
        print(str(number) + " instances of " + letter + " found in " + word)
    else:
        print(str(number) + " instance of " + letter + " found in " + word)
else:
    print("No instances of " + letter + " found in " + word)