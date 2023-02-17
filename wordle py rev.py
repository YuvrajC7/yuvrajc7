import random

# Define a list of words to choose from
words = ['apple', 'banana', 'cherry', 'durian', 'elderberry', 'fig', 'grape', 'honeydew', 'jackfruit', 'kiwi', 'lemon', 'mango', 'nectarine', 'orange', 'peach', 'pineapple', 'raspberry', 'strawberry', 'tangerine', 'watermelon']

# Choose a random word from the list
chosen_word = random.choice(words)

# Define the number of allowed guesses
num_guesses = 6

# Define the set of valid characters
valid_chars = set('abcdefghijklmnopqrstuvwxyz')

# Define a set of characters that have been guessed
guessed_chars = set()

# Define a set of correct characters
correct_chars = set(chosen_word)

# Define the set of incorrect characters
incorrect_chars = set()

# Loop until the user runs out of guesses or guesses the word
while num_guesses > 0:
    # Print the current state of the word
    current_word = ''.join(c if c in guessed_chars else '-' for c in chosen_word)
    print(f'Current word: {current_word}')
    
    # Print the number of remaining guesses
    print(f'Remaining guesses: {num_guesses}')
    
    # Get a guess from the user
    guess = input('Enter a letter: ').lower()
    
    # Check if the guess is valid
    if guess not in valid_chars:
        print('Invalid guess!')
        continue
    
    # Check if the guess has already been made
    if guess in guessed_chars:
        print('You already guessed that letter!')
        continue
    
    # Add the guess to the set of guessed characters
    guessed_chars.add(guess)
    
    # Check if the guess is correct
    if guess in correct_chars:
        print('Correct!')
        # Check if the user has won
        if guessed_chars == correct_chars:
            print(f'Congratulations! You won! The word was {chosen_word}.')
            break
    else:
        print('Incorrect!')
        # Add the guess to the set of incorrect characters
        incorrect_chars.add(guess)
        # Decrement the number of remaining guesses
        num_guesses -=1
        
# If the user runs out of guesses, print the correct word
if num_guesses == 0:
    print(f'Sorry, you lost. The word was {chosen_word}.')
