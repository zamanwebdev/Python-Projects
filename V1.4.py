import random

class Dice:
    """A simple dice class"""
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)


class DiceGame:
    """Two-player dice game with custom names"""
    def __init__(self, player1, player2, target_score=20):
        self.dice = Dice()
        self.target_score = target_score
        self.scores = {player1: 0, player2: 0}
        self.players = [player1, player2]

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
        print(f"\n🎲 Welcome to the Dice Game! First to {self.target_score} points wins.\n")
        while True:
            for player in self.players:
                input(f"{player}'s turn! Press Enter to roll...")
                self.play_turn(player)
                if self.check_winner():
                    return


def main():
    while True:
        print("\nWelcome! Enter player names.")
        player1 = input("Enter Player 1 name: ").strip()
        player2 = input("Enter Player 2 name: ").strip()

        game = DiceGame(player1, player2, target_score=20)
        game.play_game()

        replay = input("\nPlay again? [y/n]: ").strip().lower()
        if replay != "y":
            print("Thanks for playing! 👋")
            break


if __name__ == "__main__":
    main()
