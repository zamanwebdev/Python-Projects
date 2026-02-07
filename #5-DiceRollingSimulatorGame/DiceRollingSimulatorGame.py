import random

DiceRolling = True
while DiceRolling:
    print(random.randint(1, 6))
    PlayAgain = input("Would you like to play again? [y/n]")
    if PlayAgain == "y":
        continue
    elif PlayAgain == "n":
        print("Game Over!")
        break