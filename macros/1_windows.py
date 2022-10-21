# MACRO ..... :  Windows
# DESCRIPTION :  Basic Windows Functions

from keycode_win_de import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode

app = {
    'name' : 'WINDOWS',
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000000, '', []),
        (0x000000, '', []),
        (0x000000, '', []),
        # 2nd row ----------
        (0x663300, 'TSKMGR', [Keycode.CONTROL, Keycode.SHIFT, Keycode.ESCAPE]),
        (0x663300, 'DSKTP', [Keycode.WINDOWS, 'd']),
        (0x663300, 'EXPL', [Keycode.WINDOWS, 'e']),
        # 3rd row ----------
        (0x380e0e, 'SelAll', [Keycode.CONTROL, 'a']),
        (0x02180B, 'CBHist', [Keycode.WINDOWS, 'v']),
        (0x663300, 'SNIPPT', [Keycode.WINDOWS, 'r', 0.5, '%windir%\system32\SnippingTool.exe', Keycode.RETURN]),
        # 4th row ----------
        (0x380e0e, 'Cut', [Keycode.CONTROL, 'x']),
        (0x380e0e, 'Copy', [Keycode.CONTROL, 'c']),
        (0x380e0e, 'Paste', [Keycode.CONTROL, 'v']),
        # Encoder button ---
        (0x000000, 'NoSkype', [Keycode.ALT, Keycode.F4])
    ]
}


def init_module(_keyboard):
    key_sequences = []

    for sequence in key_sequences:
        for item in sequence:
            _keyboard.press(item)
