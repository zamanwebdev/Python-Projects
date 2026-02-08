import random

words = ["python", "developer", "programming", "hangman", "computer"]
word = random.choice(words)
guessed_letters = set()
chances = 6

print("🎮 Welcome to Hangman Game!")

while chances > 0:
    display_word = ""

    # Show word progress
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word.strip())
    print("Guessed letters:", " ".join(sorted(guessed_letters)))
    print("Chances left:", chances)

    guess = input("Guess a letter: ").lower().strip()

    # ---- Validation ----
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Enter only ONE alphabet letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.add(guess)

    # ---- Game Logic ----
    if guess not in word:
        chances -= 1
        print("❌ Wrong guess!")
    else:
        print("✅ Good guess!")

    # ---- Win Check ----
    if all(letter in guessed_letters for letter in word):
        print(f"\n🏆 You WON! The word was '{word}'.")
        break
else:
    print(f"\n💀 Game Over! The word was '{word}'.")
