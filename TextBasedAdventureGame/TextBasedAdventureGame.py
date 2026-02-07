answer = input("do you want to play this game? [Yes/No]:")

if answer == "Yes":
    print("welcome to the game!")
    answer = input("do you want to go jungle or cave? [jungle/cave]: ")

    if answer == "jungle":
        print("you see the hungry tiger ☺ Tiger will eat you.")
    elif answer == "cave":
        print("you seen the bean in front of cave")
        answer = input("do you want to fight with the bear or run away? [fight/run]")
        if answer == "fight":
            print("bear is too much strong! you lose the game.")
        else:
            print("Wow! Still you are alive")

else:
    print("The Game Closed")
