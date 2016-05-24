import random

class Dice:

    def __init__(self, face):

        self.face = face

    def roll(self):

        new_face = random.choice((1, 2, 3, 4, 5, 5, 6))
        self.face = new_face

