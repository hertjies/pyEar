import src.global_constants as global_constants


def test_default_configuration_file():
    assert (
        global_constants.default_configuration_file is not None
    ), "Default configuration file constant is None"
    assert (
        isinstance(global_constants.default_configuration_file, str)
    ), "Default configuration file constant is not a str"
    assert (
        global_constants.default_configuration_file != ""
    ), "Default configuration file constant is empty"


def test_default_configuration_values_available():
    values = [
        "COLOR_1",
        "COLOR_2",
        "COLOR_3",
        "COLOR_4",
        "COLOR_5",
        "COLOR_6",
        "COLOR_7",
        "COLOR_8",
        "FOCUS_LOCK",
        "FONT_FILE",
        "KEYMAP_C",
        "KEYMAP_CSHARP",
        # 'KEYMAP_DFLAT',
        "KEYMAP_D",
        "KEYMAP_DSHARP",
        # 'KEYMAP_EFLAT',
        "KEYMAP_E",
        "KEYMAP_F",
        "KEYMAP_FSHARP",
        # 'KEYMAP_GFLAT',
        "KEYMAP_G",
        "KEYMAP_GSHARP",
        # 'KEYMAP_AFLAT',
        "KEYMAP_A",
        "KEYMAP_ASHARP",
        # 'KEYMAP_BFLAT',
        "KEYMAP_B",
        "WINDOW_HEIGHT",
        "WINDOW_WIDTH",
    ]

    for const in values:
        value = global_constants.default_configuration.get(const)
        assert (
            value is not None
        ), f"Default configuration contant {value} is None"
        assert (
            isinstance(value, str)
        ), f"Default configuration contant {value} is not a str"
        assert (
            value != ""
        ), f"Default configuration contant {value} is empty"
