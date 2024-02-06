from src.config import Config

def test_read_from_file():
    this_config = Config()
    assert this_config.__load_from_file() is type(list)

