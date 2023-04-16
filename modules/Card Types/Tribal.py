from .Card import Card


class Tribal(Card):
    def __init__(self, name, cost, text, creature_type):
        super().__init__(name, cost, text)
        self.card_type = "Tribal"
        self.creature_type = creature_type
