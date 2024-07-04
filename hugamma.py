import random

def select_random_word(word_list):
    return random.choice(word_list)

def display_word_progress(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def get_guess():
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) == 1 and guess.isalpha():
            return guess
        print("Invalid input. Please enter a single letter.")

def play_hangman(word_list, max_incorrect_guesses=6):
    word = select_random_word(word_list)
    guessed_letters = set()
    incorrect_guesses = 0
    
    print("Welcome to Hangman!")
    
    while incorrect_guesses < max_incorrect_guesses:
        print(f"Word: {display_word_progress(word, guessed_letters)}")
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
        
        guess = get_guess()
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            print("Correct guess!")
            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You guessed the word: {word}")
                break
        else:
            incorrect_guesses += 1
            guessed_letters.add(guess)
            print("Incorrect guess.")
        
    if incorrect_guesses == max_incorrect_guesses:
        print(f"Sorry, you've run out of guesses. The word was: {word}")

# List of words for the game
word_list = ["python", "hangman", "challenge", "programming", "random", "difficulty"]

# Start the game
play_hangman(word_list)
