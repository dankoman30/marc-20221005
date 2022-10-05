from CLSColor import Color
from CLSWireframe import Wireframe


class Point(Wireframe):
    def __init__(self, x=0, y=0, z=0, name="Point"):
        self.X = x
        self.Y = y
        self.Z = z
        self.Name = name
        self.Color = Color
        self.Show = True
