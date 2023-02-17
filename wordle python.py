import random

# Define a list of possible words
words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]

# Select a random word from the list
chosen_word = random.choice(words)

# Define the number of tries
tries = 6

# Loop until the user guesses the word or runs out of tries
while tries > 0:
    # Get a guess from the user
    guess = input("Enter your guess: ")

    # Check if the guess is the same as the chosen word
    if guess == chosen_word:
        print("Congratulations! You guessed the word.")
        break
    else:
        # Check how many letters are in the correct position
        matches = 0
        for i in range(len(guess)):
            if guess[i] == chosen_word[i]:
                matches += 1

        # Print the number of matches and decrement the number of tries
        print("Matches: " + str(matches))
        tries -= 1

# If the user runs out of tries, print the chosen word
if tries == 0:
    print("You ran out of tries. The word was: " + chosen_word)
