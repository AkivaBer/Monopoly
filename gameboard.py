import tkinter
import tkinter as tk
from PIL import Image as PILImage, ImageTk

from Monopoly.Bank import *
from Monopoly.Player import Player
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

def init_players():
    num_players = input("How many players? ")
    if num_players.isdigit():
        num_players = int(num_players)
    else:
        num_players = ""

    if num_players == "":
        return []

    player_names = []
    for i in range(num_players):
        player_names.append(input(f"Name of player {i}: "))
    return player_names

class Gameboard:
    def __init__(self, height):
        self.height = height
        self.space_size = height / 12.34
        self.cur_player = 0
        self.popup_open = False
        self.bank = Bank()
        self.root = tk.Tk()
        self.root.title("Monopoly Board Simulation")
        self.root.minsize(width=height + 300, height=height)
        self.root.geometry("800x600")

        # Initialize players
        self.player_names = init_players()
        self.players = []
        if not self.player_names:
            self.player_names = ["AI1", "AI2", "AI3", "AI4"]

        # Create main frame to hold the canvas and player info side by side
        main_frame = tk.Frame(self.root)
        main_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Create gameboard section
        board_frame = tk.Frame(main_frame)
        board_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(board_frame, bg='green')
        self.canvas.pack(fill="both", expand=True)
        self.prev_size = min(self.canvas.winfo_width(), self.canvas.winfo_height())

        # Draw the pieces on the board
        for name in self.player_names:
            piece = Piece(self.canvas, self.space_size)
            player = Player(name, piece)
            self.players.append(player)
            piece.draw_piece()
            print(f"Piece {player.get_piece()} initial coordinates: {piece.get_piece_coordinates()}")

        # Draw the image of the board
        self.original_image = PILImage.open(r"C:\Users\akiva\PycharmProjects\MonopolyAI\Monopoly\monopoly_500.jpg")
        self.draw_grid()

        # Create player info section
        player_frame = tk.Frame(main_frame)
        self.update_player_info(player_frame)
        player_frame.pack(side=tk.RIGHT, fill="both", expand=True)

        # Create a frame for all the buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(side=tk.BOTTOM, fill=tk.X)
        roll_button = tk.Button(button_frame, text="Roll Dice", command=self.move_selected_piece)
        trade_button = tk.Button(button_frame, text="Trade", command=self.players[self.cur_player].trade)
        roll_button.pack(side=tk.LEFT, expand=True, fill=tk.X)
        trade_button.pack(side=tk.LEFT, expand=True, fill=tk.X)

        # Configure settings for a resize
        self.root.bind("<Configure>", self.resize)

    def resize(self, event):
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        size = min(canvas_width, canvas_height)

        if abs(self.prev_size - size) > 10:
            self.prev_size = size
            self.draw_grid()
            for player in self.players:
                player.get_piece().update_position(size)

    def draw_grid(self):
        self.canvas.delete("all")

        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()

        size = min(canvas_width, canvas_height)

        resized_image = self.original_image.resize((size, size))
        self.board_image = ImageTk.PhotoImage(resized_image)
        self.canvas.create_image(0, 0, anchor="nw", image=self.board_image)

    def move_selected_piece(self):
        if not self.popup_open:
            # Move the currently selected piece (first piece in the list)
            double = self.players[self.cur_player].get_piece().move_forward()
            cur_position = self.players[self.cur_player].get_piece().get_pos()
            print(f"Position is {cur_position}")

            self.execute_actions(cur_position)

            # Move on to next player
            self.cur_player = (self.cur_player + 1) % len(self.players) if not double else self.cur_player

    def execute_actions(self, cur_position):
        cur_property = self.bank.look_up_property(cur_position)
        match cur_property.card_type:
            case CardType.PROPERTY:
                self.property_popup(cur_property)
            case CardType.CHANCE:
                self.chance_utility_popup(cur_property)
            case CardType.COMMUNITY_CHEST:
                self.chance_utility_popup(cur_property)
            case CardType.JAIL:
                pass
            case CardType.JUST_VISITING:
                pass
            case CardType.RAILROAD:
                pass
            case CardType.INCOME_TAX:
                pass
            case CardType.LUXURY_TAX:
                pass
            case CardType.FREE_PARKING:
                pass
            case CardType.ELECTRIC_COMPANY:
                pass
            case CardType.WATER_WORKS:
                pass
            case CardType.GO:
                pass
            case _:
                pass

    def update_player_info(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

        for player in self.players:
            print(player)
            player_name = tk.Label(frame, text=f"{player.name}", font=("Helvetica", 14, "bold"))
            player_name.pack()

            money = tk.Label(frame, text=f"Money: ${player.money}")
            money.pack()

            property_info = tk.Label(frame, text="Properties:")
            property_info.pack()

    def property_popup(self, conv_prop):
        self.popup_open = True
        buyWindow = tk.Toplevel()
        property_info = (
            f"Property: {conv_prop.name}\n"
            f"Price: ${conv_prop.price}\n"
            f"Building Cost: ${conv_prop.build_cost}\n"
            f"Rent (no houses): ${conv_prop.std_rent}\n"
            f"Rent (1 house): ${conv_prop.one_rent}\n"
            f"Rent (2 houses): ${conv_prop.two_rent}\n"
            f"Rent (3 houses): ${conv_prop.three_rent}\n"
            f"Rent (4 houses): ${conv_prop.four_rent}\n"
            f"Rent (hotel): ${conv_prop.hotel_rent}"
        )
        label = tk.Label(buyWindow, text=property_info, justify=tk.LEFT)
        label.pack(fill='x', padx=50, pady=5)
        close = tk.Button(buyWindow, text="Close", command=lambda: self.close_property(buyWindow))
        buy = tk.Button(buyWindow, text="Buy")

        close.pack(side=tk.LEFT, fill="x", expand=True)
        buy.pack(side=tk.LEFT, fill="x", expand=True)

    def chance_utility_popup(self, conv_card):
        self.popup_open = True
        chance_comm_window = tk.Toplevel()
        chance_info = f"You have opened a {conv_card.name}"
        label = tk.Label(chance_comm_window, text=chance_info)

    def close_property(self, popup):
        self.popup_open = False
        popup.destroy()

    def run(self):
        self.root.mainloop()

