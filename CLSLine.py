from math import sqrt
from CLSColor import Color
from CLSVector import Vector
from CLSWireframe import Wireframe


class Line(Wireframe):
    def __init__(self, point1, point2, name="Line"):
        super().__init__(name)

        self.point1 = point1
        self.point2 = point2
        self.Name = name
        self.Color = Color(124, 124, 124)
        self.Show = True
        self.Length = sqrt(pow((self.point2.X - self.point1.X), 2) +
                           pow((self.point2.Y - self.point1.Y), 2) +
                           pow((self.point2.Z - self.point1.Z), 2))
        self.Vector = Vector(self.point1, self.point2)