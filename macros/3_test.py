# MACRO ..... :  Test
# DESCRIPTION :  Basic Test Functions

from keycode_win_de import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode

import ColorToggle

app = {
    'name' : 'TEST',
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        [0x000000, '', [ColorToggle.ColorToggle(0xFF0000,0x00FF00)]],
        (0x000020, '', []),
        (0x000020, '', []),
        # 2nd row ----------
        (0x000020, '', []),
        (0x000020, '', []),
        (0x000020, '', []),
        # 3rd row ----------
        (0x000020, '', []),
        (0x000020, '', []),
        (0x000020, '', []),
        # 4th row ----------
        (0x000020, '', []),
        (0x000020, '', []),
        (0x000020, '', []),
        # Encoder button ---
        (0x000000, '', [])
    ]
}

def init_module(_keyboard):
    key_sequences = []

    for sequence in key_sequences:
        for item in sequence:
            _keyboard.press(item)
