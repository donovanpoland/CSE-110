import random

# Creativity
"""
I allowed the user to play over and over again by asking if they want to play again or not.
I have a list of words and each game chooses from that list.
A high score system is implemented and stored across the game as long as you keep saying "yes" to the play again question.
I also restrict the amount of allowed guesses per round and change it depending on how long the word is for an added challange.
"""

words = ["mosiah", "nephi", "gospel", "love", "faith", "charity", "mormon", "bible", "scripture", "hope", "sacrament", "covenant", "temple", "baptism", "jesus"]
secret_word = random.choice(words) # Choose random word
letter_count = len(secret_word) # Check length of word
max_guesses = letter_count - 1 # Set max guesses
play_again = "yes" # Enter game loop
high_score = max_guesses # Set highscore

#instructions to user
print("\nWelcome to the word guessing game!\n" + 
      "You will be given a hint that will display an underscore _ representing a letter position.\n" +
      "If you enter a word with the correct lettter but wrong position it will display in lower case.\n" + 
      "If it is the correct letter and correct positon it will display in upper case. Good luck.\n")

while play_again == "yes":
    # Reset all necessary variables for the new game round
    # List to store all the hints after each guess
    hints = []  # Clear the hints for the new game
    guess_count = 0  # Reset the guess count
    letter_count = len(secret_word)  # Recalculate the letter count
    initial_hint = "_ " * letter_count  # Reset the initial hint
    guess = "" # Reset user guess to enter loop
    max_guesses = letter_count # Changes max guesses based on number of letters in the new word
    #print(f"for testing secret word is: {secret_word}")

    while guess != secret_word and guess_count < max_guesses:
        if guess_count == 0:
            print(f"You get {max_guesses} tries to find the word")
            # Display the initial hint (underscores for each letter)
            print(f"Your hint is: {initial_hint.strip()}")
            guess = input("What is your guess? ")
            guess_count += 1
        else:
            guess = input("What is your guess? ")
            guess_count += 1
        
        # Check if the length of the guess matches the secret word this wont be triggered if the length matches
        while len(guess.lower()) != letter_count:
            guess = input(f"That word does not have {letter_count} letters, please try again: ")

        hint = ['_'] * letter_count

        # First check to mark correct letters in the correct position
        for i in range(letter_count):
            if guess[i].lower() == secret_word[i].lower():
                hint[i] = guess[i].upper()

        # Second check to mark correct letters in the wrong position
        for i in range(letter_count):
            if hint[i] == '_':  # If not already matched in correct position
                if guess[i].lower() in secret_word and guess[i].lower() != secret_word[i].lower():
                    hint[i] = guess[i].lower()

        # Store the hint after each guess
        hints.append(" ".join(hint))

        # Display all hints
        print("Here are all your hints:")
        for index, each_hint in enumerate(hints, 1):
            print(f"Guess {index}: {each_hint}")

    # If the loop is exited, check if the user guessed correctly or ran out of attempts
    if guess == secret_word:
        print(f"Congratulations! You guessed the word '{secret_word.upper()}' in {guess_count} try(s).")
    else :
        print(f"You ran out of guesses, the word was '{secret_word.upper()}'")

    # Ask if the user wants to play again
    play_again = input("Can you beat your high score? Would you like to play again? (yes/no)")
    if play_again.lower() == "yes": 
        #check highscore and print        
        if guess_count < high_score:
            high_score = guess_count
            print(f"Your new high score is {high_score} try(s).\n")
        else :
            print(f"Your high score is {high_score} try(s).\n")
        
        # If yes then display that a new word has generated and then reset everything at the top.
        print("\nA new word has been generated.")
        secret_word = random.choice(words) # Choose random word

    #if this is triggered the loops ends and the program stops   
    else:
         print("Good Bye.")

