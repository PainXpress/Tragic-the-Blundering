from Card import Card


class Creature(Card):
    def __init__(self, name, cost, text, power, toughness):
        super().__init__(name, cost, text)
        self.card_type = "Creature"
        self.power = power
        self.toughness = toughness
