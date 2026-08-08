import random

# List of predefined words
words = ["python", "apple", "chair", "house", "water"]

# Randomly choose a secret word
secret_word = random.choice(words)

# Create blank display
display = ["_"] * len(secret_word)

# Number of incorrect guesses allowed
lives = 6

# Store guessed letters
guessed_letters = []

print("================================")
print("      Welcome to Hangman")
print("================================")

while lives > 0 and "_" in display:

    print("\nWord:", " ".join(display))
    print("Lives Left:", lives)

    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check if letter exists in the word
    if guess in secret_word:
        print("Correct Guess!")

        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display[i] = guess

    else:
        lives -= 1
        print("Wrong Guess!")

# Final Result
if "_" not in display:
    print("\nCongratulations! You guessed the word:", secret_word)
else:
    print("\nGame Over!")
    print("The correct word was:", secret_word)