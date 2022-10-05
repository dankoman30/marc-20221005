from CLSColor import Color
from CLSLine import Line
from CLSPoint import Point


class EntryPoint:
    point1 = Point(10, 20, 30, "MyPoint")
    print("X :", point1.X, "Y :", point1.Y, "Z :", point1.Z)

    point1.Show = False

    print("Name :", point1.Name, "Show :", point1.Show)

    point1.Color = Color(255, 123, 12)
    print("Color R :", point1.Color.R, "Color G :", point1.Color.G, "Color B :", point1.Color.B)

    point2 = Point(40, 30, 20, "MyOtherPoint")
    print("X :", point2.X, "Y :", point2.Y, "Z :", point2.Z)

    point2.Show = True

    print("Name :", point2.Name, "Show :", point2.Show)

    point2.Color = Color(255, 123, 12)
    print("Color R :", point2.Color.R, "Color G :", point2.Color.G, "Color B :", point2.Color.B)

    line1 = Line(point1, point2, "Line.1")
    print("Line Length :", line1.Length)

    