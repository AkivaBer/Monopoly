from Monopoly.Cards import *


def init_properties():
    # The Brown properties
    Mediterranean = Property("Mediterranean", 60, 50, "Brown", 2, 10, 30, 90, 160, 250, False)
    Baltic = Property("Baltic", 60, 50, "Brown", 4, 20, 60, 180, 320, 450, True)

    # The Light Blue properties
    Oriental = Property("Oriental", 100, 50, "Light Blue", 6, 30, 90, 270, 400, 550, False)
    Vermont = Property("Vermont", 100, 50, "Light Blue", 6, 30, 90, 270, 400, 550, False)
    Connecticut = Property("Connecticut", 120, 50, "Light Blue", 8, 40, 100, 300, 450, 600, True)

    # The Pink properties
    StCharles = Property("St. Charles Place", 140, 100, "Pink", 10, 50, 150, 450, 625, 750, False)
    States = Property("States Avenue", 140, 100, "Pink", 10, 50, 150, 450, 625, 750, False)
    Virginia = Property("Virginia Avenue", 160, 100, "Pink", 12, 60, 180, 500, 700, 900, True)

    # The Orange properties
    StJames = Property("St. James Place", 180, 100, "Orange", 14, 70, 200, 550, 750, 950, False)
    Tennessee = Property("Tennessee Avenue", 180, 100, "Orange", 14, 70, 200, 550, 750, 950, False)
    NewYork = Property("New York Avenue", 200, 100, "Orange", 16, 80, 220, 600, 800, 1000, True)

    # The Red properties
    Kentucky = Property("Kentucky Avenue", 220, 150, "Red", 18, 90, 250, 700, 875, 1050, False)
    Indiana = Property("Indiana Avenue", 220, 150, "Red", 18, 90, 250, 700, 875, 1050, False)
    Illinois = Property("Illinois Avenue", 240, 150, "Red", 20, 100, 300, 750, 925, 1100, True)

    # The Yellow properties
    Atlantic = Property("Atlantic Avenue", 260, 150, "Yellow", 22, 110, 330, 800, 975, 1150, False)
    Ventnor = Property("Ventnor Avenue", 260, 150, "Yellow", 22, 110, 330, 800, 975, 1150, False)
    MarvinGardens = Property("Marvin Gardens", 280, 150, "Yellow", 24, 120, 360, 850, 1025, 1200, True)

    # The Green properties
    Pacific = Property("Pacific Avenue", 300, 200, "Green", 26, 130, 390, 900, 1100, 1275, False)
    NorthCarolina = Property("North Carolina Avenue", 300, 200, "Green", 26, 130, 390, 900, 1100, 1275, False)
    Pennsylvania = Property("Pennsylvania Avenue", 320, 200, "Green", 28, 150, 450, 1000, 1200, 1400, True)

    # The Dark Blue properties
    ParkPlace = Property("Park Place", 350, 200, "Dark Blue", 35, 175, 500, 1100, 1300, 1500, False)
    Boardwalk = Property("Boardwalk", 400, 200, "Dark Blue", 50, 200, 600, 1400, 1700, 2000, True)

    properties = [
        Mediterranean, Baltic, Oriental, Vermont, Connecticut,
        StCharles, States, Virginia, StJames, Tennessee, NewYork,
        Kentucky, Indiana, Illinois, Atlantic, Ventnor, MarvinGardens,
        Pacific, NorthCarolina, Pennsylvania, ParkPlace, Boardwalk]

    Chance = ChanceComm("Chance", True)
    CommunityChest = ChanceComm("Community Chest", True)

    ReadingRail = Railroad("Reading Railroad")
    PennR = Railroad("Pennsylvania Railroad")
    BO = Railroad("B&O Railroad")
    ShortLineR = Railroad("Short Line Railroad")

    Go = Speciality("Go", "go", False, 200)
    IncomeTax = Speciality("Income Tax", "tax", True, 200)
    LuxTax = Speciality("Luxury Tax", "tax", True, 75)

    Visiting = Speciality("Just Visting", "jail", False, 0)
    FreeParking = Speciality("Free Parking", "parking", False, 0)

    Jail = Speciality("Jail", "jail", False, 0)

    ElectricCompany = Utility("Electric Company")
    WaterWorks = Utility("Water Works")

    board_positions = {
        20: Go,
        21: Mediterranean,
        22: CommunityChest,
        23: Baltic,
        24: IncomeTax,
        25: ReadingRail,
        26: Oriental,
        27: Chance,
        28: Vermont,
        29: Connecticut,
        30: Visiting,
        31: StCharles,
        32: ElectricCompany,
        33: States,
        34: Virginia,
        35: PennR,
        36: StJames,
        37: CommunityChest,  # Assuming another Community Chest position
        38: Tennessee,
        39: NewYork,
        0: FreeParking,
        1: Kentucky,
        2: Chance,  # Another Chance position
        3: Indiana,
        4: Illinois,
        5: BO,
        6: Atlantic,
        7: Ventnor,
        8: WaterWorks,
        9: MarvinGardens,
        10: Jail,
        11: Pacific,
        12: NorthCarolina,
        13: CommunityChest,  # Another Community Chest position
        14: Pennsylvania,
        15: ShortLineR,
        16: Chance,  # Assuming this position is a Chance space
        17: ParkPlace,
        18: LuxTax,
        19: Boardwalk
    }

    return board_positions


class Bank:
    def __init__(self):
        self.houses_left = 32
        self.hotels_left = 12
        self.properties = init_properties()

    def look_up_property(self, position):
        return self.properties.get(position)

        



