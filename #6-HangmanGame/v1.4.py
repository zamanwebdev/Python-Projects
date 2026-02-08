# Nightmare Mode — 50 Words Challenge
import random
import time

# 50 words list
words = [
    "python","developer","keyboard","monitor","internet","programming","software","hardware","database","network",
    "security","encryption","function","variable","constant","algorithm","compiler","debugging","framework","library",
    "package","object","class","method","syntax","exception","iteration","recursion","boolean","integer",
    "string","float","operator","condition","statement","argument","parameter","looping","array","tuple",
    "dictionary","set","module","server","client","protocol","virtual","machine","binary","process"
]

# Show all 50 words
print("🧠 Choose wisely... One of these is your mystery word:\n")
print(", ".join(words))

# Player chooses lives
while True:
    try:
        lives = int(input("\nEnter number of lives: "))
        if lives < 1:
            print("Lives must be at least 1.")
            continue
        break
    except:
        print("Enter a valid number!")

word = random.choice(words)
guessed = set()
TIME_LIMIT = 7

print("\n💀 NIGHTMARE 50-WORD MODE 💀")

while lives > 0:
    display = " ".join([l if l in guessed else "_" for l in word])
    print("\nWord:", display)
    print("Guessed:", " ".join(sorted(guessed)))
    print("Lives:", lives)

    start = time.time()
    guess = input("Guess letter: ").lower().strip()
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

    if guess not in word:
        lives -= 1
        print("Wrong guess!")
    else:
        print("Correct!")

    if all(letter in guessed for letter in word):
        print(f"\n🏆 YOU WON! Word was '{word}'")
        break

else:
    print(f"\n💀 YOU LOST! Word was '{word}'")
