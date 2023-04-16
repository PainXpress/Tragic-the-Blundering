import pygame

from modules import settings, menu, game, opponent


# Call the function to untap all permanents
untap_all_permanents()


# Initialize Pygame
pygame.init()

settings = settings.Settings()
window_width = settings.window_width
window_height = settings.window_height

# Set up the window
window = pygame.display.set_mode((settings.window_width, settings.window_height))
pygame.display.set_caption(settings.window_title)

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
