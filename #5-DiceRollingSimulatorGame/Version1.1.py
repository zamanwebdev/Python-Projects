import random

while True:
    dice = random.randint(1, 6)
    print(f"\n🎲 You rolled: {dice}")

    play_again = input("Roll again? [y/n]: ").strip().lower()

    if play_again == "y":
        continue
    elif play_again == "n":
        print("Game Over! 👋")
        break
    else:
        print("Invalid input! Please type y or n.")
