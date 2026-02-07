import random

def play_game():
    print("\n🎮 Welcome to the Number Guessing Challenge!")

    # Difficulty selection
    print("\nSelect Difficulty:")
    print("1. Easy (1–50, 10 lives)")
    print("2. Medium (1–100, 7 lives)")
    print("3. Hard (1–200, 5 lives)")

    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        max_num = 50
        lives = 10
    elif choice == "2":
        max_num = 100
        lives = 7
    else:
        max_num = 200
        lives = 5

    number = random.randint(1, max_num)
    score = lives * 10

    print(f"\n🔢 I'm thinking of a number between 1 and {max_num}")
    print(f"❤️ Lives: {lives} | ⭐ Score: {score}")

    while lives > 0:
        try:
            guess = int(input("\nEnter your guess: "))

            if guess == number:
                print(f"🎉 Correct! The number was {number}")
                print(f"🏆 Final Score: {score}")
                return

            lives -= 1
            score -= 10

            # Hint system
            if guess > number:
                print("📈 Too high!")
            else:
                print("📉 Too low!")

            # Extra hint when low lives
            if lives == 2:
                if number % 2 == 0:
                    print("💡 Hint: The number is EVEN")
                else:
                    print("💡 Hint: The number is ODD")

            print(f"❤️ Lives left: {lives}")

        except ValueError:
            print("❌ Enter numbers only!")

    print(f"\n💀 Game Over! The number was {number}")


# Replay system
while True:
    play_game()
    again = input("\n🔁 Play again? (yes/no): ").lower()
    if again != "yes":
        print("👋 Thanks for playing!")
        break
