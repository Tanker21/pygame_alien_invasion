class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self, ai_game):
        """Initializes statistics"""
        self.settings = ai_game.settings
        self.reset_stats()
        # start Alien Invasion in an inactive state
        self.game_active = False

    def reset_stats(self):
        """Initializes statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit
        
