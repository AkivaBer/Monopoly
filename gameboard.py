import tkinter as tk
from PIL import Image as PILImage, ImageTk
from Monopoly.piece import *

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

        for x in range(num_pieces_on_go):
            piece = Piece(self.canvas, self.space_size)
            self.pieces.append(piece)

        # Create a frame for the button
        button_frame = tk.Frame(self.root)
        button_frame.pack(side="bottom", fill="x")

        # Create the button within the button frame
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

    from PIL import Image, ImageTk

    # ... rest of your code ...

    def draw_grid(self):
        self.canvas.delete("all")

        # Load the image using Pillow
        pil_image = PILImage.open(r"C:\Users\akiva\PycharmProjects\MonopolyAI\Monopoly\monopoly_500.jpg")
        board_image = ImageTk.PhotoImage(pil_image)
        self.canvas.image = board_image
        self.canvas.create_image(0, 0, anchor="nw", image=board_image)

    def move_selected_piece(self):
        # Move the currently selected piece (first piece in the list)
        double = self.pieces[self.cur_piece].move_forward()
        self.cur_piece = (self.cur_piece + 1) % len(self.pieces) if not double else self.cur_piece

    def run(self):
        self.root.mainloop()
