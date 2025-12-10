import random

secret_number = random.randint(1, 50)
attempts = 5

print("🎯 Guess the Number Game!")
print("I'm thinking of a number between 1 and 50.")
print(f"You have {attempts} attempts.\n")

for i in range(attempts):

    guess_input = input("Enter your guess: ").strip()

    # If user presses enter without typing anything
    if guess_input == "":
        print("❗ Please enter a number!\n")
        continue   # Don't count this as an attempt

    # Try converting to int safely
    try:
        guess = int(guess_input)
    except ValueError:
        print("❗ Invalid input! Enter a valid number.\n")
        continue   # Don't count this as an attempt

    if guess == secret_number:
        print("🎉 Correct! You guessed the number!")
        break
    elif guess < secret_number:
        print("📉 Too low! Try again.\n")
    else:
        print("📈 Too high! Try again.\n")

else:
    print(f"❌ Out of attempts! The number was: {secret_number}")
