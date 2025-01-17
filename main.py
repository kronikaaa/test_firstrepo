import random
def guessing_game():
    number_to_guess = random.randint(1,100)
    guess_count = 0


    while True:
        user_guess = int(input("Enter your guess: "))
        guess_count += 1
        if user_guess > number_to_guess:
            print("The entered number is bigger")
        elif user_guess < number_to_guess:
            print("TheN entered number is smaller")
        else:
            print(f"Great! You guessed the number after {guess_count} attempts")
            break

guessing_game()




