from card import Card


class Permanent(Card):
    def __init__(self, name, cost, text, power, toughness, owner):
        super().__init__(name, cost, text)
        self.power = power
        self.toughness = toughness
        self.owner = owner
        self.tapped = False
        self.summoning_sick = True

    def __str__(self):
        return f"{self.name} ({self.cost}) [{self.power}/{self.toughness}]"

    def tap(self):
        self.tapped = True

    def untap(self):
        self.tapped = False

    def get_owner(self):
        return self.owner

    def is_tapped(self):
        return self.tapped

    def is_summoning_sick(self):
        return self.summoning_sick
