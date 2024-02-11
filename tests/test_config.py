from src.config import Config
import os

test_config = Config()
test_file = "tests/test_file"
test_write_data = {"my_test_key": "my_test_value"}
test_read_data = "my_test_key my_test_value"


def test_get_config():
    assert isinstance(
        test_config.configuration, dict
    ), "Configuration returned is not dictionary of of keys, values"


def test_set_config():
    test_config.set_config("COLOR_1", "Blue")
    config = test_config.get_config()
    assert config["COLOR_1"] == "Blue", "Congifuration set value returned is incorrect"


def test_write_to_file():
    write = test_config.write_to_file(test_file, test_write_data)
    assert write is True, "Failed to write to file"


def test_load_from_file():
    read = test_config.load_from_file(test_file)
    assert isinstance(read, list), "Failed to read from file and return a list of lines"
    assert isinstance(read[0], str), "Data line read from file is not a str"
    assert read[0] == test_read_data, "Data read from file is incorrect"

    os.remove(test_file)
