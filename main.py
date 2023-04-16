import pygame

from modules import settings, menu
from modules.game import untap_all_permanents
from modules.settings import Settings

# Call the function to untap all permanents
untap_all_permanents()


# Initialize Pygame
pygame.init()

my_settings = Settings()
screen = pygame.display.set_mode((my_settings.window_width, my_settings.window_height))

# Set up the window
window = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Tragic The Blundering")

# Display the menu
menu.display_menu(window)


# Run the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    window.fill(settings.bg_color)

    # Draw objects and update the screen
    pygame.display.update()

# Quit Pygame on exit
pygame.quit()
