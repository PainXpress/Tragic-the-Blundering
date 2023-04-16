from Card import Card


class Land(Card):
    def __init__(self, name, text):
        super().__init__(name, 0, text)
        self.card_type = "Land"
