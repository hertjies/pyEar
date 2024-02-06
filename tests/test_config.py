import pytest
from src.config import Config

def test_config():
    this_test_config = Config()
    assert this_test_config.load_config_from_file() is True
