from src.loader import Loader

test_loader = Loader()


def test_init_loader():
    assert isinstance(test_loader.config, object) , "Failed to initialise config for loader"
    # assert test_loader.pygame is True, "Failed to initialise pygame for loader"
    # assert test_loader.scores is True, "Failed to initialise scores for loader"
    # assert test_loader.font is True, "Failed to initialise font for loader"
    # assert test_loader.sound is True, "Failed to initialise sound for loader"
    # assert test_loader.graphics is True, "Failed to initilise graphics for loader"
