import random

# List of math questions and their answers
math_questions = [
    {"question": "What is 5 + 3?", "answer": "eight"},
    {"question": "What is 7 * 6?", "answer": "fortytwo"},
    {"question": "What is 9 - 4?", "answer": "five"},
    {"question": "What is 12 / 3?", "answer": "four"},
    {"question": "What is the square root of 81?", "answer": "nine"},
    {"question": "What is 2^3 (2 raised to the power of 3)?", "answer": "eight"},
    {"question": "What is 15 + 27?", "answer": "fortytwo"},
    {"question": "What is 100 - 25?", "answer": "seventyfive"},
    {"question": "What is 9 * 9?", "answer": "eightyone"},
    {"question": "What is 10 / 2?", "answer": "five"}
]

# Function to start the hangman game
def hangman_game():
    # Select a random math question
    question = random.choice(math_questions)
    answer = question["answer"]
    guessed_letters = set()  # Set to store guessed letters
    correct_letters = set(answer)  # Set of letters in the answer
    lives = 6  # Number of lives the player has

    print("Welcome to the Math Hangman Game!")
    print("You have to guess the answer to a math question.")
    print(f"Question: {question['question']}")
    print(f"The answer has {len(answer)} letters.")

    # Game loop
    while lives > 0 and correct_letters:
        # Display the current state of the answer
        display_word = ''.join([letter if letter in guessed_letters else '_' for letter in answer])
        print("\nCurrent word: " + ' '.join(display_word))

        # Get the player's guess
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"You've already guessed the letter '{guess}'. Try again.")
        elif guess in correct_letters:
            guessed_letters.add(guess)
            correct_letters.remove(guess)
            print(f"Good job! The letter '{guess}' is in the answer.")
        else:
            guessed_letters.add(guess)
            lives -= 1
            print(f"Wrong guess! The letter '{guess}' is not in the answer. You have {lives} lives left.")

    # Check the result of the game
    if not correct_letters:
        print(f"\nCongratulations! You correctly answered the question: {question['question']}")
        print(f"The answer was: {answer}")
    else:
        print(f"\nYou ran out of lives! The correct answer to the question '{question['question']}' was '{answer}'.")

# Run the hangman game
hangman_game()
