import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # pip install pillow

class DiceGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Dice Game 🎲")
        self.root.geometry("450x400")

        self.player1_name = tk.StringVar()
        self.player2_name = tk.StringVar()
        self.current_player = None
        self.scores = {}

        self.dice_images = [ImageTk.PhotoImage(Image.open(f"dice{i}.png").resize((100, 100))) for i in range(1, 7)]

        self.create_widgets()

    def create_widgets(self):
        # Player name input
        tk.Label(self.root, text="Enter Player 1:").pack()
        tk.Entry(self.root, textvariable=self.player1_name).pack()

        tk.Label(self.root, text="Enter Player 2:").pack()
        tk.Entry(self.root, textvariable=self.player2_name).pack()

        tk.Button(self.root, text="Start Game", command=self.start_game).pack(pady=10)

        # Dice display
        self.dice_label = tk.Label(self.root)
        self.dice_label.pack(pady=10)

        # Game info
        self.info_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.info_label.pack(pady=10)

        # Roll button
        self.roll_button = tk.Button(self.root, text="Roll Dice 🎲", state="disabled", command=self.roll_dice)
        self.roll_button.pack(pady=10)

        # Scoreboard
        self.score_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.score_label.pack(pady=10)

        # Reset button
        self.reset_button = tk.Button(self.root, text="Reset Game", state="disabled", command=self.reset_game)
        self.reset_button.pack(pady=10)

    def start_game(self):
        p1 = self.player1_name.get().strip()
        p2 = self.player2_name.get().strip()
        if not p1 or not p2:
            messagebox.showwarning("Input Error", "Please enter both player names!")
            return

        self.scores = {p1: 0, p2: 0}
        self.players = [p1, p2]
        self.current_player_index = 0
        self.current_player = self.players[self.current_player_index]

        self.info_label.config(text=f"{self.current_player}'s turn! Click Roll Dice.")
        self.update_scores()

        self.roll_button.config(state="normal")
        self.reset_button.config(state="normal")
        self.dice_label.config(image='')

    def roll_dice(self):
        roll = random.randint(1, 6)
        self.scores[self.current_player] += roll
        self.dice_label.config(image=self.dice_images[roll-1])
        self.update_scores()

        # Check winner
        if self.scores[self.current_player] >= 20:
            messagebox.showinfo("Winner 🏆", f"{self.current_player} wins with {self.scores[self.current_player]} points!")
            self.roll_button.config(state="disabled")
            return

        # Switch player
        self.current_player_index = (self.current_player_index + 1) % 2
        self.current_player = self.players[self.current_player_index]
        self.info_label.config(text=f"{self.current_player}'s turn! Click Roll Dice.")

    def update_scores(self):
        score_text = f"{self.players[0]}: {self.scores[self.players[0]]}  |  {self.players[1]}: {self.scores[self.players[1]]}"
        self.score_label.config(text=score_text)

    def reset_game(self):
        self.player1_name.set("")
        self.player2_name.set("")
        self.info_label.config(text="")
        self.score_label.config(text="")
        self.roll_button.config(state="disabled")
        self.reset_button.config(state="disabled")
        self.dice_label.config(image='')


if __name__ == "__main__":
    root = tk.Tk()
    game = Dic
