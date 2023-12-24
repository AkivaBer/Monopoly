import random
from Monopoly.Dice import *

colors = ['white', 'black', 'red', 'green', 'blue', 'cyan', 'yellow', 'magenta']
class Piece:
    def __init__(self, canvas, space_size):
        self.canvas = canvas
        self.space_size = space_size
        self.piece_radius = self.space_size // 5
        self.position = 0  # Initial position
        self.color = random.choice(colors)
        colors.remove(self.color)
        self.draw_piece()

    def draw_piece(self):
        x, y = self.get_piece_coordinates()
        self.piece = self.canvas.create_oval(
            x, y,
            x + self.piece_radius * 2, y + self.piece_radius * 2,
            fill=self.color
        )

    def resize(self, space_size):
        self.space_size = space_size
        self.piece_radius = space_size // 5

    def move_forward(self):
        roll, double = roll_dice()
        self.position = (self.position + roll) % 40
        self.canvas.delete(self.piece)  # Clear the old piece
        self.draw_piece()
        return double

    def get_piece_coordinates(self):
        row = self.position // 10
        col = self.position % 10

        # Top Row
        if row == 0:
            x = (col * self.space_size) + (self.space_size / 2 - self.piece_radius)
            y = (self.space_size / 2 - self.piece_radius)
        # Right column
        elif row == 1:
            x = (11 * self.space_size) - (self.space_size / 2 + self.piece_radius)
            y = col * self.space_size + self.piece_radius
        # Bottom Row
        elif row == 2:
            x = (10 - col) * self.space_size + self.piece_radius
            y = (11 * self.space_size) - (self.space_size / 2 + self.piece_radius)
        # Left column
        else:
            x = self.piece_radius
            y = (10 - col) * self.space_size + self.piece_radius
        return x, y
