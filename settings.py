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
        self.ship_limit = 3

        # bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 80, 80, 80
        self.bullets_allowed = 3

        # alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction == 1 to the right, -1 to the left
        self.fleet_direction = 1
