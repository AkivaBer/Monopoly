import tkinter as tk
from Monopoly.piece import *
from Monopoly.Dice import *

class Gameboard:
    def __init__(self, height, num_pieces_on_go=1):
        self.height = height
        self.space_size = height // 11
        self.corner_size = self.space_size + 10
        self.pieces = []
        self.cur_piece = 0

        self.root = tk.Tk()
        self.root.title("Monopoly Board Simulation")

        self.root.minsize(width=height, height=height + 25)

        board_frame = tk.Frame(self.root)
        board_frame.pack(side="top", fill="both", expand=True)

        self.canvas = tk.Canvas(board_frame, bg='green')
        self.canvas.pack(fill="both", expand=True)
        self.draw_grid()

        self.root.bind("<Configure>", self.resize)
        # Create and initialize pieces on the "Go" square
        for x in range(num_pieces_on_go):
            piece = Piece(self.canvas, self.space_size)
            self.pieces.append(piece)

        button_frame = tk.Frame(self.root)
        button_frame.pack(side="bottom", fill="x")

        button = tk.Button(button_frame, text="Roll Dice", command=self.move_selected_piece)
        button.pack(side="bottom", fill="x")

    def resize(self, event):
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        self.height = min(canvas_width, canvas_height)
        self.space_size = self.height // 11
        self.corner_size = self.space_size

        # Redraw the grid and pieces
        self.draw_grid()
        for piece in self.pieces:
            piece.resize(self.space_size)
            piece.draw_piece()

    def draw_grid(self):
        self.canvas.delete("all")

        # Draw top vertical lines
        self.canvas.create_line(self.space_size, 0, self.space_size, self.height)
        for i in range(2, 11):
            self.canvas.create_line(i * self.space_size, 0, i * self.space_size, self.height // 11)

        # Left Horizontal Lines
        self.canvas.create_line(0, self.space_size, self.height, self.space_size, fill="black")
        for i in range(1, 11):
            self.canvas.create_line(0, i * self.space_size, self.height // 11, i * self.space_size, fill="black")

        # Draw bottom vertical lines
        for i in range(1, 10):
            self.canvas.create_line(i * self.space_size, 10 * self.space_size, i * self.space_size,
                                    self.height, fill="black")
        self.canvas.create_line(10 * self.space_size, 0, 10 * self.space_size, self.height, fill="black")

        # Right horizontal lines
        for i in range(1, 10):
            self.canvas.create_line(10 * self.space_size, i * self.space_size, self.height,
                                    i * self.space_size, fill="black")
        self.canvas.create_line(0, 10 * self.space_size, self.height, 10 * self.space_size, fill="black")

        self.canvas.create_line(self.height, 0, self.height, self.height)
        self.canvas.create_line(0, self.height, self.height, self.height)

    def move_selected_piece(self):
        # Move the currently selected piece (first piece in the list)
        double = self.pieces[self.cur_piece].move_forward()
        self.cur_piece = (self.cur_piece + 1) % len(self.pieces) if not double else self.cur_piece

    def run(self):
        self.root.mainloop()
