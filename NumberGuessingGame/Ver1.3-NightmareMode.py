import random
import time

def nightmare_mode():
    print("\n👹 NIGHTMARE MODE ACTIVATED 👹")
    print("Rules are brutal...")

    max_num = 500
    number = random.randint(1, max_num)
    lives = 1
    score = 100

    print(f"\n🔢 Guess the number between 1 and {max_num}")
    print("☠ You have ONE life")
    print("⏳ You have 5 seconds per guess\n")

    while lives > 0:
        start_time = time.time()

        try:
            guess = int(input("Enter your guess: "))

            # Time check
            if time.time() - start_time > 5:
                print("⏰ TOO SLOW!")
                lives = 0
                break

            # Wrong guess penalty
            if guess != number:
                score -= 25

                # Fake hint system (mind game)
                if random.choice([True, False]):
                    print("💡 Hint: You're VERY close... (maybe 😈)")
                else:
                    print("💡 Hint: You're FAR away... (or are you?)")

                lives -= 1
            else:
                print(f"\n🎉 YOU BEAT NIGHTMARE MODE! Number was {number}")
                print(f"🏆 Final Score: {score}")
                return

        except ValueError:
            print("❌ Numbers only!")

    print(f"\n💀 GAME OVER. The number was {number}")


# Run game
nightmare_mode()
