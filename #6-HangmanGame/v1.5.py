import random
import time

print("💀 CUSTOM NIGHTMARE HANGMAN 💀")

while True:  # 🔁 Game restart loop

    # ---- Player chooses lives ----
    while True:
        try:
            lives = int(input("\nEnter number of lives: "))
            if lives < 1:
                print("Lives must be at least 1.")
                continue
            break
        except ValueError:
            print("Enter a valid number!")

    # ---- Player enters 10 words ----
    print("\nEnter 10 words for the game (letters only):")
    user_words = []

    while len(user_words) < 10:
        word = input(f"Word {len(user_words)+1}: ").lower().strip()
        if not word.isalpha():
            print("Only alphabet words allowed!")
            continue
        user_words.append(word)

    print("\n🧠 Word list:", ", ".join(user_words))

    secret_word = random.choice(user_words)
    guessed = set()
    TIME_LIMIT = 7

    print("\n🔥 Game Start!")

    # ---- Game loop ----
    while lives > 0:
        display = " ".join([l if l in guessed else "_" for l in secret_word])
        print("\nWord:", display)
        print("Guessed:", " ".join(sorted(guessed)))
        print("Lives:", lives)

        start = time.time()
        guess = input("Guess a letter: ").lower().strip()
        end = time.time()

        if end - start > TIME_LIMIT:
            lives -= 1
            print("⏰ Too slow!")
            continue

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input!")
            continue

        if guess in guessed:
            lives -= 1
            print("Repeated guess penalty!")
            continue

        guessed.add(guess)

        if guess not in secret_word:
            lives -= 1
            print("Wrong guess!")
        else:
            print("Correct!")

        if all(letter in guessed for letter in secret_word):
            print(f"\n🏆 YOU WON! Word was '{secret_word}'")
            break

    else:
        print(f"\n💀 GAME OVER! Word was '{secret_word}'")

    # ---- Replay Option ----
    again = input("\nDo you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for playing! 👋")
        break
