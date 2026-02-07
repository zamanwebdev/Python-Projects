import random

roll_count = 0

while True:
    roll = random.randint(1, 6)
    roll_count += 1

    print(f"\n🎲 Roll #{roll_count}: {roll}")

    if input("Roll again? [y/n]: ").strip().lower() != "y":
        print(f"Game Over! Total rolls: {roll_count}")
        break
