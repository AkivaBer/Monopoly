from Monopoly.Cards import Property


def init_properties():
    # The Brown properties
    Mediterranean = Property(60, 50, "Brown", 2, 10, 30, 90, 160, 250, False)
    Baltic = Property(60, 50, "Brown", 4, 20, 60, 180, 320, 450, True)

    # The Light Blue properties
    Oriental = Property(100, 50, "Light Blue", 6, 30, 90, 270, 400, 550, False)
    Vermont = Property(100, 50, "Light Blue", 6, 30, 90, 270, 400, 550, False)
    Connecticut = Property(120, 50, "Light Blue", 8, 40, 100, 300, 450, 600, True)

    # The Pink properties
    StCharles = Property(140, 100, "Pink", 10, 50, 150, 450, 625, 750, False)
    States = Property(140, 100, "Pink", 10, 50, 150, 450, 625, 750, False)
    Virginia = Property(160, 100, "Pink", 12, 60, 180, 500, 700, 900, True)

    # The Orange properties
    StJames = Property(180, 100, "Orange", 14, 70, 200, 550, 750, 950, False)
    Tennessee = Property(180, 100, "Orange", 14, 70, 200, 550, 750, 950, False)
    NewYork = Property(200, 100, "Orange", 16, 80, 220, 600, 800, 1000, True)

    # The Red properties
    Kentucky = Property(220, 150, "Red", 18, 90, 250, 700, 875, 1050, False)
    Indiana = Property(220, 150, "Red", 18, 90, 250, 700, 875, 1050, False)
    Illinois = Property(240, 150, "Red", 20, 100, 300, 750, 925, 1100, True)

    # The Yellow properties
    Atlantic = Property(260, 150, "Yellow", 22, 110, 330, 800, 975, 1150, False)
    Ventnor = Property(260, 150, "Yellow", 22, 110, 330, 800, 975, 1150, False)
    MarvinGardens = Property(280, 150, "Yellow", 24, 120, 360, 850, 1025, 1200, True)

    # The Green properties
    Pacific = Property(300, 200, "Green", 26, 130, 390, 900, 1100, 1275, False)
    NorthCarolina = Property(300, 200, "Green", 26, 130, 390, 900, 1100, 1275, False)
    Pennsylvania = Property(320, 200, "Green", 28, 150, 450, 1000, 1200, 1400, True)

    # The Dark Blue properties
    ParkPlace = Property(350, 200, "Dark Blue", 35, 175, 500, 1100, 1300, 1500, False)
    Boardwalk = Property(400, 200, "Dark Blue", 50, 200, 600, 1400, 1700, 2000, True)

    properties = [
        Mediterranean, Baltic, Oriental, Vermont, Connecticut,
        StCharles, States, Virginia, StJames, Tennessee, NewYork,
        Kentucky, Indiana, Illinois, Atlantic, Ventnor, MarvinGardens,
        Pacific, NorthCarolina, Pennsylvania, ParkPlace, Boardwalk
    ]

    return properties

class Bank:
    def __init__(self):
        self.houses_left = 32
        self.hotels_left = 12
        self.properties = init_properties()

    def sell_house(self, player):



