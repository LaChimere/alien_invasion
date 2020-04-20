class Settings:
    # This class stores all settings of Alien Invasion

    def __init__(self):
        # initialize settings of game
        # screen settings
        self.screen_width = 1360
        self.screen_height = 768
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_speed_factor = 1.5

        # bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 80, 80, 80
        self.bullets_allowed = 3