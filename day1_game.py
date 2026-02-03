import random

def welcome_player():
    print("Welcome to the Number Guessing Game!")
    print("Try to guess the number I'm thinking of.")

def choose_difficulty():
    print("\nChoose a difficulty level:")
    print("1 - Easy (1–10)")
    print("2 - Medium (1–50)")
    print("3 - Hard (1–100)")

    level = input("Enter 1, 2, or 3: ")

    if level == "1":
        return 10
    elif level == "2":
        return 50
    elif level == "3":
        return 100
    else:
        print("Invalid choice, defaulting to Easy.")
        return 10

def play_game(high_score):
    max_number = choose_difficulty()
    number = random.randint(1, max_number)
    guess = None
    guesses_taken = 0

    print(f"\nI'm thinking of a number between 1 and {max_number}.")

    while guess != number:
        guess = int(input("Take a guess: "))
        guesses_taken += 1

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Nice job, you got it in {guesses_taken} guesses!")

        # Give a hint after 3 guesses
        if guesses_taken == 3 and guess != number:
            low_hint = max(number - 5, 1)
            high_hint = min(number + 5, max_number)
            print(f"💡 Hint: The number is between {low_hint} and {high_hint}")

    # Update high score
    if high_score is None or guesses_taken < high_score:
        high_score = guesses_taken
        print(f"🎉 New high score: {high_score} guesses!")
    else:
        print(f"Your current high score: {high_score} guesses")

    return high_score

def main():
    welcome_player()
    high_score = None

    while True:
        high_score = play_game(high_score)
        again = input("\nDo you want to play again? (yes/no): ").lower()

        if again != "yes":
            print("Thanks for playing! See you next time 👋")
            break

main()
