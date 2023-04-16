import pygame
import wx


class MenuItem:
    def __init__(self, text, font, pos):
        self.text = text
        self.font = font
        self.pos = pos
        self.color = (0, 0, 0)

        # Create surface for item text and get rect
        self.surface = self.font.render(self.text, True, self.color)
        self.rect = self.surface.get_rect()
        self.rect.center = self.pos

    def draw(self, surface):
        # Draw item on surface
        surface.blit(self.surface, self.rect)

    def on_click(self):
        # Call the appropriate function when item is clicked
        if self.text == "Play":
            # TODO: Add code to start game
            print("Starting game...")
        elif self.text == "Options":
            # TODO: Add code to open options menu
            print("Opening options menu...")
        elif self.text == "Quit":
            # Quit game
            pygame.quit()
            exit()
        elif self.text == "Deck Building":
            # TODO: Add code to open deck building menu
            print("Opening deck building menu...")
            app = wx.App()
            frame = wx.Frame(None, title='Deck Building Menu')
            frame.Show()
            app.MainLoop()


class Menu:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

        # Load the background image
        self.background = pygame.image.load("assets/images/menu background.png").convert()

        # Create font for menu items
        self.font = pygame.font.Font(None, 48)

        # Set up menu items
        self.play_item = MenuItem("Play", self.font, (self.screen_width / 2, self.screen_height / 2 - 100))
        self.options_item = MenuItem("Options", self.font, (self.screen_width / 2, self.screen_height / 2 - 50))
        self.deck_building_item = MenuItem("Deck Building", self.font, (self.screen_width / 2, self.screen_height / 2))
        self.quit_item = MenuItem("Quit", self.font, (self.screen_width / 2, self.screen_height / 2 + 50))

        # Create list of menu items
        self.menu_items = [self.play_item, self.options_item, self.deck_building_item, self.quit_item]

    def draw(self, surface):
        # Draw background image
        surface.blit(self.background, (0, 0))

        # Draw menu items on surface
        for item in self.menu_items:
            item.draw(surface)

    def handle_event(self, event):
        # Handle events
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Get mouse position
            mouse_pos = pygame.mouse.get_pos()
            # Check if mouse is clicking on a menu item
            for item in self.menu_items:
                if item.rect.collidepoint(mouse_pos):
                    # Call the function associated with the clicked item
                    item.on_click()


def display_menu(surface):
    # Initialize Pygame
    pygame.init()

    # Set up the window
    screen_width = surface.get_width()
    screen_height = surface.get_height()
    pygame.display.set_caption("Menu Test")
    window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    # Create the menu
    menu = Menu(screen_width, screen_height)

    # Run the menu loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                # Handle menu events
                menu.handle_event(event)

        # Draw the menu
        menu.draw(window)
        pygame.display.update()

    # Quit Pygame
    pygame.quit()
