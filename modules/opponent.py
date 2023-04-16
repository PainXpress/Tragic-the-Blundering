import random


class Opponent:
    def __init__(self, name):
        self.name = name
        self.life_total = 20
        self.hand = []
        self.library = []
        self.graveyard = []
        self.exile = []
        self.battlefield = []

    def draw_card(self):
        if self.library:
            card = self.library.pop(0)
            self.hand.append(card)
            return card

    def shuffle_library(self):
        random.shuffle(self.library)

    def lose_life(self, amount):
        self.life_total -= amount

    def gain_life(self, amount):
        self.life_total += amount

    def play_card(self, card):
        if card in self.hand:
            self.hand.remove(card)
            self.battlefield.append(card)

    def discard_card(self, card):
        if card in self.hand:
            self.hand.remove(card)
            self.graveyard.append(card)
