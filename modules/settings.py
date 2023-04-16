class Settings:
    """A class to store all game settings."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.bg_color = (230, 230, 230)

        # Card settings
        self.card_width = 100
        self.card_height = 140

        # Player settings
        self.player_life = 20
        self.player_mana = 0

        # Window settings
        self.window_title = "Tragic the Blundering"
        self.window_width = 1920
        self.window_height = 1080

        # Colors
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
