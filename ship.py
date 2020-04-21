import pygame


class Ship:

    def __init__(self, ai_settings, screen):
        # initialize ship and set its location
        self.screen = screen
        self.ai_settings = ai_settings

        # load ship image and get its outline rectangle
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # put each new-created ship at the bottom center of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # store float value in 'center' of the ship
        self.center = float(self.rect.centerx)

        # moving tag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # adjust the location of ship according to its moving tag
        # update 'center' of the ship
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # update rect according to self.center
        self.rect.centerx = self.center

    def blitme(self):
        # draw ship at the given location
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """make ship at the center of screen"""
        self.center = self.screen_rect.centerx
