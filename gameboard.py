import tkinter as tk
from PIL import Image as PILImage, ImageTk
from tkinter import messagebox

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
        self.player_frame = tk.Frame(main_frame)
        self.update_player_info(self.player_frame)
        self.player_frame.pack(side=tk.RIGHT, fill="both", expand=True)

        # Create a frame for all the buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(side=tk.BOTTOM, fill=tk.X)
        roll_button = tk.Button(button_frame, text="Roll Dice", command=self.move_selected_piece)
        trade_button = tk.Button(button_frame, text="Trade", command=lambda: self.trade_popup())
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
        print("Excuting action")
        cur_property = self.bank.look_up_property(cur_position)
        match cur_property.card_type:
            case CardType.PROPERTY:
                self.property_popup(cur_property)
            case CardType.CHANCE:
                self.chance_comm_popup(cur_property)
            case CardType.COMMUNITY_CHEST:
                self.chance_comm_popup(cur_property)
            case CardType.JAIL:
                self.jail_popup(cur_property)
            case CardType.JUST_VISITING:
                pass
            case CardType.RAILROAD:
                self.property_popup(cur_property)
            case CardType.INCOME_TAX:
                pass
            case CardType.LUXURY_TAX:
                pass
            case CardType.FREE_PARKING:
                pass
            case CardType.ELECTRIC_COMPANY:
                self.property_popup(cur_property)
            case CardType.WATER_WORKS:
                self.property_popup(cur_property)
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

            property_info = tk.Label(frame, text="Properties: " + str(player.properties))
            property_info.pack()

    def property_popup(self, conv_prop):
        self.popup_open = True
        buyWindow = tk.Toplevel()

        # Based on the specific property type show different information
        shown_string = ""
        if conv_prop.card_type == CardType.PROPERTY:
            shown_string = (
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
        elif conv_prop.card_type == CardType.RAILROAD:
            shown_string = (
                f"Property: {conv_prop.name}\n"
                f"Cost: $200\n"
                f"Base Rent: $50\n"
                f"Rent (Two Railroads): $100\n"
                f"Rent (Three Railroads): $150\n"
                f"Rent (Four Railroads): $200\n"
                f"Mortgage Value: $100"
            )
        else:
            shown_string = (
                f"Property: {conv_prop.name}\n"
                f"Cost: ${conv_prop.price}\n"
                "If ONE Utility is owned, rent is 4 times the number on the dice which landed the player on the "
                "utility.\n"
                "If BOTH Utilities are owned, rent is 10 times the amount shown on the dice."
            )

        label = tk.Label(buyWindow, text=shown_string,
                         justify=tk.LEFT)
        label.pack(fill='x', padx=50, pady=5)
        close = tk.Button(buyWindow, text="Close", command=lambda: self.close_property(buyWindow))
        buy = tk.Button(buyWindow, text="Buy", command=lambda: self.purchase_property(buyWindow, conv_prop))

        close.pack(side=tk.LEFT, fill="x", expand=True)
        buy.pack(side=tk.LEFT, fill="x", expand=True)

    def chance_comm_popup(self, conv_card):
        self.popup_open = True
        chance_comm_window = tk.Toplevel()
        chance_info = f"You have opened a {conv_card.name}"
        label = tk.Label(chance_comm_window, text=chance_info)
        label.pack(fill='x', padx=50, pady=5)

        close = tk.Button(chance_comm_window, text="Close", command=lambda: self.close_property(chance_comm_window))
        close.pack(side=tk.LEFT, fill="x", expand=True)

    def trade_popup(self):
        if not self.popup_open:
            self.popup_open = True
            trade_window = tk.Toplevel()
            trade_window.title("Trade")

            tk.Label(trade_window, text=f"{self.players[self.cur_player].name}'s Turn to Trade").pack()

            # Step 1: Choose trade partner
            tk.Label(trade_window, text="Choose a player to trade with:").pack()
            trade_partner_var = tk.StringVar()
            trade_partner_menu = tk.OptionMenu(trade_window, trade_partner_var,
                                               *[p.name for p in self.players if p != self.players[self.cur_player]])
            trade_partner_menu.pack()

            def proceed_to_trade():
                trade_partner_name = trade_partner_var.get()
                if not trade_partner_name:
                    return
                trade_partner = next(p for p in self.players if p.name == trade_partner_name)
                self.setup_trade_window(trade_window, trade_partner)

            proceed_button = tk.Button(trade_window, text="Proceed", command=proceed_to_trade)
            proceed_button.pack()

    def setup_trade_window(self, trade_window, trade_partner):
        # Step 2: Choose properties and money to trade
        trade_window.destroy()
        trade_window = tk.Toplevel()
        trade_window.title("Trade Details")

        tk.Label(trade_window, text=f"{self.players[self.cur_player].name} trading with {trade_partner.name}").pack()

        cur_player_give_var = tk.StringVar()
        trade_partner_give_var = tk.StringVar()

        tk.Label(trade_window, text="Select properties and money to trade:").pack()

        cur_player_frame = tk.Frame(trade_window)
        cur_player_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        tk.Label(cur_player_frame, text=f"{self.players[self.cur_player].name} gives:").pack()

        cur_player_props = tk.Listbox(cur_player_frame, selectmode="multiple")
        for prop in self.players[self.cur_player].properties:
            cur_player_props.insert(tk.END, prop)
        cur_player_props.pack()

        cur_add = tk.Button(cur_player_frame, text="+")
        cur_add.pack()
        cur_player_money = tk.Entry(cur_player_frame, textvariable=cur_player_give_var)
        cur_player_money.pack()
        cur_player_give_var.set("0")

        trade_partner_frame = tk.Frame(trade_window)
        trade_partner_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        tk.Label(trade_partner_frame, text=f"{trade_partner.name} gives:").pack()

        trade_partner_props = tk.Listbox(trade_partner_frame, selectmode="multiple")
        for prop in trade_partner.properties:
            trade_partner_props.insert(tk.END, prop)
        trade_partner_props.pack()

        trade_partner_money = tk.Entry(trade_partner_frame, textvariable=trade_partner_give_var)
        trade_partner_money.pack()
        trade_partner_give_var.set("0")

        def finalize_trade():
            cur_player_selected_props = [cur_player_props.get(i) for i in cur_player_props.curselection()]
            trade_partner_selected_props = [trade_partner_props.get(i) for i in trade_partner_props.curselection()]

            try:
                cur_player_money_val = int(cur_player_give_var.get())
                trade_partner_money_val = int(trade_partner_give_var.get())
            except ValueError:
                tk.messagebox.showerror("Invalid input", "Please enter valid money amounts")
                return

            if cur_player_money_val > self.players[
                self.cur_player].money or trade_partner_money_val > trade_partner.money:
                tk.messagebox.showerror("Insufficient funds",
                                        "One of the players does not have enough money for this trade")
                return

            if not set(cur_player_selected_props) <= set(self.players[self.cur_player].properties) or not set(
                    trade_partner_selected_props) <= set(trade_partner.properties):
                tk.messagebox.showerror("Invalid properties", "One of the players does not own the selected properties")
                return

            self.confirm_trade(trade_window, cur_player_selected_props, cur_player_money_val,
                               trade_partner_selected_props, trade_partner_money_val, trade_partner)

        finalize_button = tk.Button(trade_window, text="Finalize Trade", command=finalize_trade)
        finalize_button.pack()

    def confirm_trade(self, trade_window, cur_player_selected_props, cur_player_money_val, trade_partner_selected_props,
                      trade_partner_money_val, trade_partner):
        # Step 3: Confirm trade
        trade_window.destroy()
        confirm_window = tk.Toplevel()
        confirm_window.title("Confirm Trade")

        cur_player = self.players[self.cur_player]
        trade_details = (
            f"{cur_player.name} gives: {cur_player_selected_props}, ${cur_player_money_val}\n"
            f"{trade_partner.name} gives: {trade_partner_selected_props}, ${trade_partner_money_val}\n"
        )
        tk.Label(confirm_window, text="Confirm Trade:").pack()
        tk.Label(confirm_window, text=trade_details).pack()

        def complete_trade():
            # Execute the trade
            exchange_money(cur_player, trade_partner, cur_player_money_val, trade_partner_money_val)

            cur_player.edit_properties(remove=True, property_list=cur_player_selected_props, util_list=[],
                                       railroad_list=[])
            cur_player.edit_properties(remove=False, property_list=trade_partner_selected_props, util_list=[],
                                       railroad_list=[])
            trade_partner.edit_properties(remove=True, property_list=trade_partner_selected_props, util_list=[],
                                          railroad_list=[])
            trade_partner.edit_properties(remove=False, property_list=cur_player_selected_props, util_list=[],
                                          railroad_list=[])

            self.update_player_info(self.player_frame)
            self.close_property(confirm_window)

        confirm_button = tk.Button(confirm_window, text="Confirm", command=complete_trade)
        cancel_button = tk.Button(confirm_window, text="Cancel", command=lambda: self.close_property(confirm_window))

        confirm_button.pack(side=tk.LEFT, expand=True, fill=tk.X)
        cancel_button.pack(side=tk.RIGHT, expand=True, fill=tk.X)

    def jail_popup(self, conv_card):
        self.popup_open = True

    def close_property(self, popup):
        self.popup_open = False
        popup.destroy()

    def purchase_property(self, window, cur_property):
        if not is_owned(cur_property):
            confirm = self.players[self.cur_player].buy_property(cur_property)
            cur_property.set_owner(self.players[self.cur_player]) if confirm else print("Property can't be bought")

        self.update_player_info(self.player_frame)
        self.close_property(window)

    def run(self):
        self.root.mainloop()
