import random

class Die(object):
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

    def num_sides(self):
        return self.sides

    def __str__(self):
        return str(self.sides)


def roll_dice(sides=6):
    d1 = Die(sides)
    d2 = Die(sides)

    d1_roll = d1.roll()
    d2_roll = d2.roll()

    double = True if d1_roll == d2_roll else False

    total = d1_roll + d2_roll
    print(f"Die Roll is: {total}, Double = {double}")
    return total, double
