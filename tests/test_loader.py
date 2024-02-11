from src.loader import Loader

test_loader = Loader()


def test_init_loader():
    assert test_loader.config is True, "Failed to initialise config for loader"
    assert test_loader.scores is True, "Failed to initialise scores for loader"
    assert test_loader.font is True, "Failed to initialise font for loader"
    assert test_loader.sound is True, "Failed to initialise sound for loader"
    assert test_loader.graphics is True, "Failed to initilise graphics for loader"


def test_config_loader():
    assert (
        test_loader.load_instance_config() is True
    ), "Failed call to load condig for loader"


def test_scores_loader():
    assert (
        test_loader.load_instance_scores() is True
    ), "Failed call to load scores for loader"


def test_font_loader():
    assert (
        test_loader.load_instance_font() is True
    ), "Failed call to load font for loader"


def test_sound_loader():
    assert (
        test_loader.load_instance_sound() is True
    ), "Failed call to load sound for loader"


def test_graphics_loader():
    assert (
        test_loader.load_instance_graphics() is True
    ), "Failed call to load graphics from loader"
