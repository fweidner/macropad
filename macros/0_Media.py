# MACRO ..... : Media
# DESCRIPTION :

from keycode_win_de import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode

import ColorToggle

app = {
    'name' : 'MEDIA',
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x02180B, 'DFLT', [Keycode.CONTROL, Keycode.SHIFT, Keycode.ALT, Keycode.F11]),
        (0x02180B, 'IDLE', [Keycode.CONTROL, Keycode.SHIFT, Keycode.ALT, Keycode.F9]),
        (0x02180B, 'BRB', [Keycode.CONTROL, Keycode.SHIFT, Keycode.ALT, Keycode.F10]),
        # 2nd row ----------
        (0x000020, 'Vol-', [Keycode.CONTROL, Keycode.F19]),
        [0x770000, 'SPKR', [Keycode.CONTROL, Keycode.F17, ColorToggle.ColorToggle(0x770000, 0x007700)]],
        (0x000020, 'Vol+', [Keycode.CONTROL, Keycode.F18,]),
        # 3rd row ----------
        (0x000020, 'Vol-', [Keycode.CONTROL, Keycode.F15]),
        [0x770000, 'HDPHNS', [Keycode.CONTROL, Keycode.F13, ColorToggle.ColorToggle(0x770000, 0x007700)]],
        (0x000020, 'Vol+', [Keycode.CONTROL, Keycode.F14]),
        # 4th row ----------
        (0x100020, 'PL-PS', [[ConsumerControlCode.PLAY_PAUSE]]),
        (0x02180B, 'WERK', [Keycode.CONTROL, Keycode.SHIFT, Keycode.ALT, Keycode.F2]),
        [0x770000, 'MUTE', [Keycode.CONTROL, Keycode.F21, ColorToggle.ColorToggle(0x770000, 0x007700)]],

        # Encoder button ---
        (0x000000, '', [])
    ]
}
# Write your code here :-)

def init_module(_keyboard):
    key_sequences = []
    print("init")

    #speaker
    key_sequences.append([Keycode.CONTROL, Keycode.F20])

    #headphone
    key_sequences.append([Keycode.CONTROL, Keycode.F16])

    #microphone
    key_sequences.append([Keycode.CONTROL, Keycode.F22])

    for sequence in key_sequences:
        for item in sequence:
            _keyboard.press(item)
