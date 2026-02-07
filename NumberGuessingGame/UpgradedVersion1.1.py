import random

randomNumber = random.randrange(1, 200)
attempts = 0

print("🎯 Guess the number between 1 and 199")

while True:
    try:
        userInput = int(input("Enter your guess: "))
        attempts += 1

        if userInput > randomNumber:
            print("📈 Too high! Try again.")
        elif userInput < randomNumber:
            print("📉 Too low! Try again.")
        else:
            print(f"✅ Correct! The number was {randomNumber}")
            print(f"🏆 You guessed it in {attempts} attempts!")
            break

    except ValueError:
        print("❌ Please enter a valid number!")
