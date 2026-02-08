import random
import time

words = {
    "algorithm": "Step-by-step problem solving method",
    "pneumonia": "A serious lung disease",
    "awkward": "Socially uncomfortable",
    "rhythm": "Music without normal vowels",
    "oxygen": "You need this to survive"
}

word, hint = random.choice(list(words.items()))
guessed = set()
lives = 5
TIME_LIMIT = 7  # seconds per guess

print("💀 HANGMAN NIGHTMARE MODE 💀")
print("You have 5 lives. Each guess must be within 7 seconds!")
print("Type '?' for a hint (costs 1 life)\n")

while lives > 0:
    display = " ".join([letter if letter in guessed else "_" for letter in word])
    print("\nWord:", display)
    print("Guessed:", " ".join(sorted(guessed)))
    print("Lives:", lives)

    start = time.time()
    guess = input("Enter letter: ").lower().strip()
    end = time.time()

    # ⏳ Time check
    if end - start > TIME_LIMIT:
        lives -= 1
        print("⏰ TOO SLOW! You lost a life!")
        continue

    # Hint system
    if guess == "?":
        lives -= 1
        print(f"💡 HINT: {hint}")
        continue

    # Validation
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Invalid input!")
        continue

    if guess in guessed:
        lives -= 1
        print("⚠️ Repeated guess! Nightmare doesn't forgive!")
        continue

    guessed.add(guess)

    if guess not in word:
        lives -= 1
        print("🔥 Wrong guess!")
    else:
        print("✅ Correct!")

    # Win check
    if all(letter in guessed for letter in word):
        print(f"\n🏆 YOU SURVIVED NIGHTMARE MODE! Word was '{word}'")
        break

else:
    print(f"\n💀 YOU DIED. The word was '{word}'")
