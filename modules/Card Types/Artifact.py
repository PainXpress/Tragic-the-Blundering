from Card import Card


class Artifact(Card):
    def __init__(self, name, cost, text, card_type="Artifact"):
        super().__init__(name, cost, text, card_type)
        self.subtype = None
        self.rarity = None
        self.power = None
        self.toughness = None
