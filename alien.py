import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and set its rect attribute
        try:
            self.image = pygame.image.load('images/alien.bmp')
        except pygame.error as e:
            print(f"Error loading alien image: {e}")
            self.image = pygame.Surface((30, 30))  # Fallback: green square
            self.image.fill((0, 255, 0))

        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen with padding
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position as a float
        self.x = float(self.rect.x)

    def update(self):
        """Move the alien left or right."""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = int(self.x)  # Convert float to int for pixel precision

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
        return False