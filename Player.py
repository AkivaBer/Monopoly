class Player:
    def __init__(self, name, piece):
        self.name = name
        self.piece = piece
        self.money = 1500
        self.properties = []
        self.mortg_properties = []
        self.get_out_of_jail = 0
        self.railroads_owned = []
        self.util_owned = []
        self.in_jail = 0

    def get_total_railroads_owned(self):
        return len(self.railroads_owned)

    def edit_properties(self, remove, property_list, util_list, railroad_list):
        if remove:
            self.properties = [prop for prop in self.properties if prop not in property_list]
            self.railroads_owned = [rail for rail in self.railroads_owned if rail not in railroad_list]
            self.util_owned = [util for util in self.util_owned if util not in util_list]
        else:
            self.properties.extend(property_list)
            self.railroads_owned.extend(railroad_list)
            self.util_owned.extend(util_list)

    def edit_bank(self, remove, amount):
        if remove and amount >= self.money:
            self.money -= amount
            return self.money
        elif not remove:
            self.money += amount
            return self.money

        return 0

    def get_piece(self):
        return self.piece
    def has_properties(self, prop_list):
        return set(prop_list) <= set(self.properties)

    def trade(self):
        pass
    def player_info(self):
        return {self.name: {"money": self.money, "properties": [self.properties]}}


