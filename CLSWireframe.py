from CLSColor import Color


class Wireframe:
    def __init__(self, color=Color, show=True, name="Default"):
        self.Name = name
        self.Color = color
        self.Show = show
