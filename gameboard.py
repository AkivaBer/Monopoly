import tkinter as tk
from PIL import Image as PILImage, ImageTk
from Monopoly.piece import *

monopoly_board = [
    "Free Parking", "Kentucky Avenue", "Chance", "Indiana Avenue", "Illinois Avenue",
    "B. & O. Railroad", "Atlantic Avenue", "Ventnor Avenue", "Water Works", "Marvin Gardens",
    "Go to Jail", "Pacific Avenue", "North Carolina Avenue", "Community Chest", "Pennsylvania Avenue",
    "Short Line", "Chance", "Park Place", "Luxury Tax", "Boardwalk",
    "Go", "Mediterranean Avenue", "Community Chest", "Baltic Avenue", "Income Tax",
    "Reading Railroad", "Oriental Avenue", "Chance", "Vermont Avenue", "Connecticut Avenue",
    "Jail / Just Visiting", "St. Charles Place", "Electric Company", "States Avenue", "Virginia Avenue",
    "Pennsylvania Railroad", "St. James Place", "Community Chest", "Tennessee Avenue", "New York Avenue"
]
class Gameboard:
    def __init__(self, height, num_pieces_on_go=1):
        self.height = height
        self.space_size = height / 12.34
        self.pieces = []
        self.cur_piece = 0

        self.root = tk.Tk()
        self.root.title("Monopoly Board Simulation")
        self.root.minsize(width=height, height=height + 25)

        board_frame = tk.Frame(self.root)
        board_frame.pack(side="top", fill="both", expand=True)

        self.canvas = tk.Canvas(board_frame, bg='green')
        self.canvas.pack(fill="both", expand=True)
        self.prev_size = min(self.canvas.winfo_width(), self.canvas.winfo_height())

        for x in range(num_pieces_on_go):
            piece = Piece(self.canvas, self.space_size)
            self.pieces.append(piece)
            print(f"Piece {x} initial coordinates: {piece.get_piece_coordinates(0)}")

        self.original_image = PILImage.open(r"C:\Users\akiva\PycharmProjects\MonopolyAI\Monopoly\monopoly.jpg")
        self.draw_grid()

        self.root.bind("<Configure>", self.resize)


            # Create a frame for the button
        button_frame = tk.Frame(self.root)
        button_frame.pack(side="bottom", fill="x")

        # Create the button within the button frame
        button = tk.Button(button_frame, text="Roll Dice", command=self.move_selected_piece)
        button.pack(side="bottom", fill="x")

    def resize(self, event):
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        size = min(canvas_width, canvas_height)

        if abs(self.prev_size - size) > 10:
            self.prev_size = size
            self.draw_grid()
            for piece in self.pieces:
                piece.update_position(size, (canvas_width - size) / 2)

    def draw_grid(self):
        self.canvas.delete("all")

        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()

        size = min(canvas_width, canvas_height)

        resized_image = self.original_image.resize((size, size))
        self.board_image = ImageTk.PhotoImage(resized_image)

        # Calculate position to center the image
        x = (canvas_width - size) // 2
        y = (canvas_height - size) // 2

        self.canvas.create_image(x, y, anchor="nw", image=self.board_image)

    def move_selected_piece(self):
        # Move the currently selected piece (first piece in the list)
        double = self.pieces[self.cur_piece].move_forward()
        print(f"Position is {self.pieces[self.cur_piece].get_pos()} "
              f"which means you landed on landed on {monopoly_board[self.pieces[self.cur_piece].get_pos()]}")
        self.cur_piece = (self.cur_piece + 1) % len(self.pieces) if not double else self.cur_piece


    def run(self):
        self.root.mainloop()
