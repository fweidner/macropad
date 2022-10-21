# MACRO ..... :  Windows
# DESCRIPTION :  Basic Windows Functions

from keycode_win_de import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode

app = {
    'name' : 'POMO',
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x200000, 'DFN', [Keycode.RIGHT_ALT, Keycode.RIGHT_SHIFT, Keycode.F5]),
        (0x02180B, 'WERK', [Keycode.CONTROL, Keycode.SHIFT, Keycode.ALT, Keycode.F12]),
        (0x02180B, 'DFLT', [Keycode.CONTROL, Keycode.SHIFT, Keycode.ALT, Keycode.F11]),
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
