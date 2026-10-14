
import random
from collections import Counter
import os

def number_guessing_game():
    print("\n===== NUMBER GUESSING GAME =====")
    number = random.randint(1, 100)
    attempts = 0
    score = 100

    print("Guess a number between 1 and 100!")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number:
                print("Too low! Try a higher number.")
                score -= 10
            elif guess > number:
                print("Too high! Try a lower number.")
                score -= 10
            else:
                print(f"Correct! You guessed it in {attempts} attempts.")
                print(f"Your score: {max(score, 0)}")
                break

        except ValueError:
            print("Please enter a valid number.")

def word_counter():
    print("\n===== WORD COUNTER =====")
    filename = input("Enter text file name (example: sample.txt): ")

    if not os.path.exists(filename):
        print("File not found! Create the text file first.")
        return

    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()

    words = text.lower().split()
    frequency = Counter(words)

    print("\nTotal words:", len(words))
    print("Unique words:", len(frequency))
    print("\nWord frequency:")

    for word, count in frequency.most_common():
        print(f"{word}: {count}")

def main():
    while True:
        print("\n===== PYTHON MINI PROJECT =====")
        print("1. Number Guessing Game")
        print("2. Word Counter")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            number_guessing_game()
        elif choice == "2":
            word_counter()
        elif choice == "3":
            print("Thank you for using the program!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
