word = "Python"
chance = 5
GuessAdd = []
done = False
while not done:
    for letter in word:
        if letter.lower() in GuessAdd:
            print(letter, end=" ")
        else:
            print("_", end="")
    MyGuess = input(f"Your Chances is {chance}, Guess the letter : ")
    GuessAdd.append(MyGuess.lower())
    if MyGuess.lower() not in word.lower():
        chance -= 1
        if chance == 0:
            break
    done = True
    for letter in word:
        if letter.lower() not in GuessAdd:
            done = False
if done:
    print(f"Yes have won the Game, the word is {word}")
else:
    print(f"You loos the Game, the word is {word}")

