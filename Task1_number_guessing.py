import random

def guess_the_number():
    print("Welcome to the Number Guessing Game!")
    player_name = input("Enter your name: ")

    while True:
        # Generate a random number between 1 and 100
        secret_number = random.randint(1, 100)
        attempts = 0

        print(f"\nHello, {player_name}! I've selected a number between 1 and 100. Try to guess it!")

        while attempts < 10:
            try:
                user_guess = int(input("\nEnter your guess: "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            attempts += 1

            if user_guess == secret_number:
                print(f"Congratulations, {player_name}! You've guessed the number {secret_number} correctly in {attempts} attempts.")
                break
            elif user_guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")

        if attempts == 10:
            print(f"\nSorry, {player_name}. You've run out of attempts. The correct number was {secret_number}.")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    guess_the_number()
