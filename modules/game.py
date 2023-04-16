import pygame

from modules.menu import MenuItem
from modules.opponent import Opponent
from player import Player
from modules import settings

# Initialize Pygame
pygame.init()

# Set up the window
screen = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
pygame.display.set_caption(settings.WINDOW_TITLE)

# Load the background image
background_image = pygame.image.load("assets/images/menu_background.png").convert()

# Resize the background image to fit the window
background_image = pygame.transform.scale(background_image, (settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))

# Create the game objects
all_sprites = pygame.sprite.Group()
player = Player("Player")
opponent = Opponent("Opponent")
all_sprites.add(player)
all_sprites.add(opponent)

# Set up the game
player.shuffle_library()
opponent.shuffle_library()
for i in range(7):
    player.draw_card()
    opponent.draw_card()

class Permanent:
    def __init__(self):
        self.tapped = True

    def untap(self):
        self.tapped = False


# create a new permanent
my_permanent = Permanent()

# untap the permanent
my_permanent.untap()

# check if the permanent is untapped
print(my_permanent.tapped)  # should print False

# Create the menu
class Menu:
    def __init__(self, surface):
        self.surface = surface
        self.font = pygame.font.Font(None, 48)
        self.menu_items = ["Start Game", "Options", "Quit"]
        self.selected_item = 0

        # Load the background image
        self.background = pygame.image.load("assets/images/menu background.png").convert()

        # Scale the background image to fit the screen
        self.background = pygame.transform.scale(self.background, (settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))

        # Create font for menu items
        self.font = pygame.font.Font(None, 48)

        # Set up menu items
        self.play_item = MenuItem("Play", self.font, (settings.WINDOW_WIDTH / 2, settings.WINDOW_HEIGHT / 2 - 50))
        self.options_item = MenuItem("Options", self.font, (settings.WINDOW_WIDTH / 2, settings.WINDOW_HEIGHT / 2))
        self.quit_item = MenuItem("Quit", self.font, (settings.WINDOW_WIDTH / 2, settings.WINDOW_HEIGHT / 2 + 50))

        # Create list of menu items
        self.menu_items = [self.play_item, self.options_item, self.quit_item]

    def draw(self):
        # Draw background image
        self.surface.blit(self.background, (0, 0))

        for i, item in enumerate(self.menu_items):
            color = (255, 255, 255) if i != self.selected_item else (255, 0, 0)
            text = self.font.render(item.text, True, color)
            x = (settings.WINDOW_WIDTH - text.get_width()) / 2
            y = (settings.WINDOW_HEIGHT / 2) + i * 50
            self.surface.blit(text, (x, y))

        # Draw menu items on surface
        for item in self.menu_items:
            item.draw(self.surface)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected_item = (self.selected_item - 1) % len(self.menu_items)
            elif event.key == pygame.K_DOWN:
                self.selected_item = (self.selected_item + 1) % len(self.menu_items)
            elif event.key == pygame.K_RETURN:
                if self.selected_item == 0:
                    run_game_loop()
                elif self.selected_item == 1:
                    print("Options menu not yet implemented")
                elif self.selected_item == 2:
                    pygame.quit()
                    quit()


def handle_menu_clicks(menu_items):
    for i, item in enumerate(menu_items):

        if item.rect.collidepoint(pygame.mouse.get_pos()):

            if i == 0:

                run_game_loop()

            elif i == 1:

                print("Options menu not yet implemented")

            elif i == 2:

                pygame.quit()

                quit()


def handle_game_events(player, opponent):
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            return False

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:

                return False

            elif event.key == pygame.K_SPACE:

                player.play_card()

            elif event.key == pygame.K_q:

                player.end_turn()

        elif event.type == pygame.MOUSEBUTTONDOWN and player.turn:

            mouse_pos = pygame.mouse.get_pos()

            for card in player.hand:

                if card.rect.collidepoint(mouse_pos):
                    player.play_card(card)

    return True


def run_game_loop():
    running = True

    while running:
        # Handle events

        running = handle_game_events(player, opponent)

        # Draw the screen

        screen.blit(background_image, (0, 0))

        all_sprites.draw(screen)

        player.draw_hand(screen)

        opponent.draw_hand(screen)

        player.draw_library(screen)

        opponent.draw_library(screen)

        player.draw_graveyard(screen)

        opponent.draw_graveyard(screen)

        player.draw_life(screen)

        opponent.draw_life(screen)

        pygame.display.flip()

    # Quit Pygame when loop is finished

    pygame.quit()


def run_menu_loop(menu):
    menu_running = True

    while menu_running:

        # Draw the menu

        menu.draw()

        # Handle events

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                menu_running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:

                handle_menu_clicks(menu.menu_items)

        # Update the screen

        pygame.display.update()

    # Quit Pygame when loop is finished

    pygame.quit()

    # Create a menu object


menu = Menu(screen)

# Run the menu loop

run_menu_loop(menu)
