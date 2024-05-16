import random
from Monopoly.Dice import *

colors = ['white', 'black', 'red', 'green', 'blue', 'cyan', 'yellow', 'magenta']


class Piece:
    def __init__(self, canvas, space_size):
        self.canvas = canvas
        self.space_size = space_size
        self.corner_size = 1.67 * self.space_size
        self.piece_radius = self.space_size // 5
        self.position = 20
        self.color = random.choice(colors)
        colors.remove(self.color)
        self.draw_piece()

    def draw_piece(self, offset_x=0):
        x, y = self.get_piece_coordinates()  # Assuming initial offset is 0, 0
        self.piece = self.canvas.create_oval(
            x, y,
            x + self.piece_radius * 2, y + self.piece_radius * 2,
            fill=self.color
        )
        self.canvas.update_idletasks()

    def update_position(self, size):
        self.canvas.delete(self.piece)  # Clear the old piece
        self.space_size = size / 12.34
        self.piece_radius = self.space_size // 5
        self.corner_size = 1.67 * self.space_size
        self.draw_piece()

    def move_forward(self):
        roll, double = roll_dice()
        print(f"{self.color} moving forward {roll} Double = {double}")
        self.position = (self.position + roll) % 40
        self.canvas.delete(self.piece)  # Clear the old piece
        self.draw_piece()
        return double

    def get_pos(self):
        return self.position

    def get_piece_coordinates(self):
        section = self.position // 10
        col = self.position % 10

        if section == 0:  # Top Row
            if col == 0:
                x = self.corner_size / 2
            else:
                x = self.corner_size + (col - 1) * self.space_size + (self.space_size * 1.5)
            y = self.space_size / 2 - self.piece_radius

        elif section == 1:  # Right column
            x = (10 * self.space_size) + self.corner_size / 2
            if section == 0:  # Corners
                y = self.corner_size + 9 * self.space_size + (self.corner_size / 2)
            else:
                y = self.corner_size + (col - 1) * self.space_size + self.space_size / 2

        elif section == 2:  # Bottom Row
            if col == 0:
                x = self.corner_size + 9 * self.space_size + self.corner_size / 2
            else:
                x = self.corner_size + (9 - col) * self.space_size + (self.space_size / 2.5)
            y = self.corner_size + (9 * self.space_size) + self.corner_size / 2

        else:  # Left column
            x = self.space_size / 2 - self.piece_radius
            if section == 0:  # Corners
                y = self.corner_size + (9 - col) * self.space_size + self.corner_size / 2
            else:  # Regular spaces
                y = self.corner_size + (9 - col) * self.space_size + self.space_size / 2

        return x, y
