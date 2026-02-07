import random
randomNumber = random.randrange(1,200)
# print(randomNumber)
userInput = int(input("Guess the number: "))
if userInput > randomNumber:
    print(f"Random Number is {randomNumber}")
    print("Your guess is too high")
elif userInput < randomNumber:
    print(f"Random Number is {randomNumber}")
    print("Your guess is too low")
else:
    print(f"Random Number is {randomNumber}")
    print("You guessed correctly")