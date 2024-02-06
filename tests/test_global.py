import src.global_constants as global_constants

def test_all_global_values_available():
    values = ['COLOR_1',
        'COLOR_2',
        'COLOR_3',
        'COLOR_4',
        'COLOR_5',
        'COLOR_6',
        'COLOR_7',
        'COLOR_8',
        'FOCUS_LOCK',
        'FONT_FILE',
        'KEYMAP_C',
        'KEYMAP_CSHARP',
        'KEYMAP_DFLAT',
        'KEYMAP_D',
        'KEYMAP_DSHARP',
        'KEYMAP_EFLAT',
        'KEYMAP_E',
        'KEYMAP_F',
        'KEYMAP_FSHARP',
        'KEYMAP_GFLAT',
        'KEYMAP_G',
        'KEYMAP_GSHARP',
        'KEYMAP_AFLAT',
        'KEYMAP_A',
        'KEYMAP_ASHARP',
        'KEYMAP_BFLAT',
        'KEYMAP_B',
        'WINDOW_HEIGHT',
        'WINDOW_WIDTH',
        ]
    
    for const in values:
        value = getattr(global_constants, const)
        assert value is not None