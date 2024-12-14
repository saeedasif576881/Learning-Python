def display_progress(word, guessed_letters):
    """
    Displays the current progress of the word with guessed letters and underscores.
    """
    progress = ""
    for letter in word:
        if letter in guessed_letters:
            progress += letter + " "
        else:
            progress += "_ "
    return progress.strip()

def validate_input(guess):
    """
    Validates the player's input to ensure it is a single alphabetical character.
    """
    if len(guess) != 1 or not guess.isalpha():
        return False
    return True
