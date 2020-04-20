import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    # this class charges shot bullets
    def __init__(self, ai_settings, screen, ship):
        # create a bullet object at which ship locates
        super(Bullet, self).__init__()
        self.screen = screen

        # create a rectangle representing a bullet at (0, 0), and set its location correctly
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # store the location of bullet
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        # move up the bullet
        # update the location
        self.y -= self.speed_factor
        # update the 'rect' location
        self.rect.y = self.y

    def draw_bullet(self):
        # draw bullet on screen
        pygame.draw.rect(self.screen, self.color, self.rect)
