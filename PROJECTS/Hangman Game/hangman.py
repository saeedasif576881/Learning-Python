import hangman_util  # Utility module
import random

def play_hangman():
    word_list = ["python", "hangman", "coding", "rocket", "clouds"]
    secret_word = random.choice(word_list)
    guessed_letters = set()
    lives = 6

    print("Welcome to Hangman!")
    print("Your word is:")
    print(hangman_util.display_progress(secret_word, guessed_letters))

    while lives > 0 and "_" in hangman_util.display_progress(secret_word, guessed_letters):
        guess = input("\nEnter a letter: ").lower()

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
        elif guess in secret_word:
            print(f"Good guess! '{guess}' is in the word.")
            guessed_letters.add(guess)
        else:
            lives -= 1
            print(f"Wrong guess! '{guess}' is not in the word. Lives left: {lives}")
            guessed_letters.add(guess)

        # Show progress
        print(hangman_util.display_progress(secret_word, guessed_letters))

    if "_" not in hangman_util.display_progress(secret_word, guessed_letters):
        print("\nCongratulations! You guessed the word:", secret_word)
    else:
        print("\nGame over! The word was:", secret_word)

# Entry point
if __name__ == "__main__":
    play_hangman()
