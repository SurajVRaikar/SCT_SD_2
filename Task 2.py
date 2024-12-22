import random

def main():
    print("Welcome to the Guess the Number Game!")
    lower_bound = 1
    upper_bound = 100
    random_number = random.randint(lower_bound, upper_bound)
    attempts = 0

    print(f"I have selected a number between {lower_bound} and {upper_bound}. Can you guess it?")

    while True:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            if user_guess < lower_bound or user_guess > upper_bound:
                print(f"Please guess a number within the range {lower_bound}-{upper_bound}.")
            elif user_guess < random_number:
                print("Too low! Try again.")
            elif user_guess > random_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
