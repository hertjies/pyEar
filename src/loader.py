"""
Module for loading and initialising instances of external program requirements from disk/memory
ie: Configuration, Player data (scores), Assets (Sound, GFX)
"""

from config import Config

class Loader:
    """
    Main instance loader class
    """

    def __init__(self) -> None:
        self.config = self.load_instance_config()
        self.scores = self.load_instance_scores()
        self.font = self.load_instance_font()
        self.sound = self.load_instance_sound()
        self.graphics = self.load_instance_graphics()


    def load_instance_config(self) -> None:
        """
        Load a configuration instance
        """
        return True


    def load_instance_scores(self) -> None:
        """
        Load a player score instance
        """
        return True


    def load_instance_font(self) -> None:
        """
        Load a font instance
        """
        return True


    def load_instance_sound(self) -> None:
        """
        Load a sound store instance
        """
        return True


    def load_instance_graphics(self) -> None:
        """
        Load a graphics store instance
        """
        return True