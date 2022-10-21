class ColorToggle:

    is_toggled = False
    color_a = "0xFF0000"
    color_b = "0x0000FF"

    def __init__(self, _color_a, _color_b):
        self.color_a = _color_a
        self.color_b = _color_b

    def toggle_color(self):

        new_color = ""

        if self.is_toggled:
            self.is_toggled = False
            new_color = self.color_a
        else:
            self.is_toggled = True
            new_color = self.color_b

        self.set_color(new_color)
        #print("toggle color")
        return new_color

    def set_color(self, _color):
        print(_color)



