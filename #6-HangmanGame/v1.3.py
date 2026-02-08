import random
import time

words = {
    "algorithm": "Step-by-step problem solving method",
    "pneumonia": "A serious lung disease",
    "awkward": "Socially uncomfortable",
    "rhythm": "Music without normal vowels",
    "oxygen": "You need this to survive"
}

# ---- Player chooses lives ----
while True:
    try:
        lives = int(input("Enter number of lives (3–10 recommended): "))
        if lives < 1:
            print("Lives must be at least 1.")
            continue
        break
    except ValueError:
        print("Enter a valid number!")

word, hint = random.choice(list(words.items()))
guessed = set()
TIME_LIMIT = 7

print("\n💀 HANGMAN NIGHTMARE MODE 💀")
print(f"You have {lives} lives. Each guess must be within {TIME_LIMIT} seconds!")
print("Type '?' for a hint (costs 1 life)\n")

while lives > 0:
    display = " ".join([letter if letter in guessed else "_" for letter in word])
    print("\nWord:", display)
    print("Guessed:", " ".join(sorted(guessed)))
    print("Lives:", lives)

    start = time.time()
    guess = input("Enter letter: ").lower().strip()
    end = time.time()

    # ⏳ Time limit check
    if end - start > TIME_LIMIT:
        lives -= 1
        print("⏰ TOO SLOW! You lost a life!")
        continue

    # 💡 Hint system
    if guess == "?":
        lives -= 1
        print(f"💡 HINT: {hint}")
        continue

    # ❌ Validation
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input!")
        continue

    # 🔥 Repeated guess penalty
    if guess in guessed:
        lives -= 1
        print("Repeated guess! Nightmare penalty!")
        continue

    guessed.add(guess)

    if guess not in word:
        lives -= 1
        print("Wrong guess!")
    else:
        print("Correct!")

    # 🏆 Win check
    if all(letter in guessed for letter in word):
        print(f"\n🏆 YOU SURVIVED! Word was '{word}'")
        break

else:
    print(f"\n💀 GAME OVER. The word was '{word}'")
