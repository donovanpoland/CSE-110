import random

random_number = random.randint(1, 100)
play_again = "yes"
high_score = 100

#number = 7
guess_count = 1

print("A random integer between 1 and 100 will be generated every round, guess the number and win.")
#convert all user input of the magic number to floats to prevent the user from breaking the code by typing a float
guess = float(input("What is the magic number? "))

while play_again == "yes":
    while guess != random_number:
        #every guess will add to guess counter
        guess_count += 1
        #testing
        #print(random_number)
        if guess >= 1 and guess <= 100:
            if guess < random_number:
                print("Nope, Higher.")
                guess = float(input("What is the magic number? "))
            else :
                print("Nope, Lower.")
                guess = float(input("What is the magic number? "))
        else:
            guess = float(input("That is not a number between 1 and 100, please try again. "))
    guess_count + 1
    print(f"Correct! The magic number was {random_number}. You guessed the magic number in {guess_count} guesses!")
    play_again = input("Can you beet your high score? Would you like to play again? ")
    if play_again.lower() == "yes": 
        #check high score and print        
        if guess_count < high_score:
            high_score = guess_count
            print(f"Your new high score is {high_score}.")
        else :
            print(f"Your high score is {high_score}.")
        #change random number in case user decides to play again
        random_number = random.randint(1, 100)
        print("A new number has been generated.")
        #reset guess count
        guess_count = 1
        guess = float(input("What is the magic number? "))    
    else:
         print("Good Bye.")





