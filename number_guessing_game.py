"""Task 3: Number Guessing Game
Guess the random number between 1 and 100. Multiple rounds supported.
"""
import random


def play_round():
    secret = random.randint(1, 100)
    attempts = 0
    print("\nI'm thinking of a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Please enter a valid whole number.")
            continue

        attempts += 1  # count every valid guess

        if guess < secret:
            print("Too low! Try again.")
        elif guess > secret:
            print("Too high! Try again.")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            return attempts


def main():
    print("=== Number Guessing Game ===")
    best = None
    while True:
        attempts = play_round()
        if best is None or attempts < best:
            best = attempts
        print(f"Best score so far: {best} attempts")

        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()