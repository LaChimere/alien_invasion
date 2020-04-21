import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """class for a single alien"""

    def __init__(self, ai_settings, screen):
        """initialize an alien and set its location"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # load the image of alien, and set its 'rect'
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # the alien is near the northwest corner at the beginning
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the accurate location of alien
        self.x = float(self.rect.x)

    def blitme(self):
        """draw an alien at the given position"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """if the alien reaches the edge of screen, return True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """move aliens to the left or right"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x
