class GameStats:
    """collect infos about the game"""

    def __init__(self, ai_settings):
        """initialize infos"""
        self.ai_settings = ai_settings
        self.reset_stats()

        self.game_active = False

    def reset_stats(self):
        """initialize infos that can be changed when running the game"""
        self.ships_left = self.ai_settings.ship_limit
