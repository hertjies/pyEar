"""
Module for loading and initialising instances in a specific order of external program requirements
ie: Configuration, Player data (scores), Assets (Sound, GFX)
"""
import logging
from src.config import Config

class Loader:
    """
    Main instance loader class
    """

    config = None
    pygame = None
    scores = None
    font = None
    sound = None
    graphics = None

    def __init__(self) -> None:
        if self.config is None:
            self.config = Config()
            logging.info("Loader: set config")
        else:
            logging.warning("Loader: config already set")