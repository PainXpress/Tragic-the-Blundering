from .Card import Card

class Enchantment(Card):
    def __init__(self, name, cost, text):
        super().__init__(name, cost, text)
        self.card_type = "Enchantment"
