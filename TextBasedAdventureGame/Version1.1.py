while True:
    answer = input("Do you want to play this game? [Yes/No]: ").strip().lower()

    if answer != "yes":
        print("The Game Closed 👋")
        break

    print("Welcome to the game!")

    choice = input("Do you want to go jungle or cave? [jungle/cave]: ").strip().lower()

    if choice == "jungle":
        print("You see a hungry tiger 😈")
        print("Tiger will eat you. Game Over!")

    elif choice == "cave":
        print("You see a bear in front of the cave")

        action = input("Do you want to fight or run? [fight/run]: ").strip().lower()

        if action == "fight":
            print("Bear is too strong! You lose the game.")
        elif action == "run":
            print("Wow! You escaped. Still you are alive 🎉")
        else:
            print("Invalid action!")

    else:
        print("Invalid place!")

    again = input("Do you want to play again? [Yes/No]: ").strip().lower()
    if again != "yes":
        print("Thanks for playing! 👋")
        break
