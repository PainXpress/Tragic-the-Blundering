from Card import Card


class Planeswalker(Card):
    def __init__(self, name, cost, text, loyalty):
        super().__init__(name, cost, text)
        self.card_type = "Planeswalker"
        self.loyalty = loyalty
