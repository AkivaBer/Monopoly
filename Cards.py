from re import match

cards = []


class Property:
    """
    price, build_cost, color, one_rent, two_rent, three_rent, four_rent, hotel_rent
    """

    def __init__(self, name, card_type, price, build_cost, color, std_rent, one_rent, two_rent, three_rent, four_rent,
                 hotel_rent,
                 keystone):
        self.name = name
        self.card_type = card_type
        self.price = price
        self.build_cost = build_cost
        self.color = color
        self.houses = 0
        self.hotel = 0
        self.owner = ""
        self.std_rent = std_rent
        self.one_rent = one_rent
        self.two_rent = two_rent
        self.three_rent = three_rent
        self.four_rent = four_rent
        self.hotel_rent = hotel_rent
        self.keystone = keystone

    def get_rent(self):
        if self.houses == 0:
            return self.std_rent
        elif self.houses == 1:
            return self.one_rent
        elif self.houses == 2:
            return self.two_rent
        elif self.houses == 3:
            return self.three_rent
        elif self.houses == 4:
            return self.four_rent
        elif self.hotel == 1:
            return self.hotel_rent
        return 0

    def get_owner(self):
        if self.owner == "":
            return "UNOWNED"
        return self.owner

    def set_owner(self, new_owner):
        self.owner = new_owner

    def build_houses(self, num_houses):
        if self.houses + num_houses > 5 or self.hotel == 1:
            return -1
        self.houses += num_houses
        if self.houses == 5:
            self.houses = 0
            self.hotel = 1
        return self.houses

    def sell_houses(self, num_houses):
        if self.hotel == 0 and num_houses <= self.houses:
            self.houses -= num_houses
        elif self.hotel == 1 and num_houses <= 4:
            self.hotel = 0
            num_houses -= 1

            self.houses -= num_houses

        return self.build_cost * num_houses // 2


class Speciality:
    def __init__(self, name, card_type, bankowed, amount):
        self.name = name
        self.card_type = card_type
        self.bankOwed = bankowed
        self.earn = amount


class ChanceComm:
    def __init__(self, name, card_type, chance):
        self.name = name
        self.chance = chance
        self.card_type = card_type


class Railroad:
    def __init__(self, name, price, card_type):
        self.base_rent = 50
        self.name = name
        self.price = price
        self.card_type = card_type
        self.owner = ""

    def set_owner(self, new_owner):
        self.owner = new_owner

    def get_rent(self, player):
        # Rent depends on the number of railroads owned
        return 50 * player.get_total_railroads_owned()


class Utility:
    def __init__(self, name, price, card_type):
        self.name = name
        self.price = price
        self.card_type = card_type
        self.owner = ""

    def set_owner(self, new_owner):
        self.owner = new_owner
