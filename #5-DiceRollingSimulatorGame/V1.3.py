import random

class Dice:
    """A simple dice class"""
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)


class DiceGame:
    """Two-player dice game"""
    def __init__(self, target_score=20):
        self.dice = Dice()
        self.target_score = target_score
        self.scores = {"Player 1": 0, "Player 2": 0}

    def play_turn(self, player):
        roll = self.dice.roll()
        self.scores[player] += roll
        print(f"{player} rolled a {roll} → Total: {self.scores[player]}")

    def check_winner(self):
        for player, score in self.scores.items():
            if score >= self.target_score:
                print(f"\n🏆 {player} wins with {score} points!")
                return True
        return False

    def play_game(self):
        print(f"🎲 Welcome to the Dice Game! First to {self.target_score} points wins.\n")
        while True:
            for player in self.scores:
                input(f"{player}'s turn! Press Enter to roll...")
                self.play_turn(player)
                if self.check_winner():
                    return


def main():
    while True:
        game = DiceGame(target_score=20)
        game.play_game()

        replay = input("\nPlay again? [y/n]: ").strip().lower()
        if replay != "y":
            print("Thanks for playing! 👋")
            break


if __name__ == "__main__":
    main()
