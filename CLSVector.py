from math import sqrt
from CLSPoint import Point


class Vector:
    I = 0
    J = 0
    K = 1
    Length = 1

    def __init__(self, *args):
        if len(args) == 0:  # 0 arguments passed
            self.UnitVector = self.get_unit_vector()
        elif (len(args) == 1) and all(isinstance(value, Point) for value in args):  # 1 point passed
            self.initWith1Point(args[0])
        elif (len(args) == 2) and all(isinstance(value, Point) for value in args):  # 2 points passed
            self.initWith2Points(args[0], args[1])
        elif (len(args) == 3) and all(isinstance(value, (int, float, complex)) for value in args):  # 3 numeric values passed
            self.initWithXYZ(args[0], args[1], args[2])

    def initWith1Point(self, point):
        self.I = point.X
        self.J = point.Y
        self.K = point.Z
        self.Length = self.get_length(0, point.X, 0, point.Y, 0, point.Z)
        self.UnitVector = self.get_unit_vector()

    def initWith2Points(self, point1, point2):
        self.I = point2.X - point1.X
        self.J = point2.Y - point1.Y
        self.K = point2.Z - point1.Z
        self.Length = self.get_length(point2.X, point1.X, point2.Y, point1.Y, point2.Z, point1.Z)
        self.UnitVector = self.get_unit_vector()

    def initWithXYZ(self, i, j, k):
        self.I = i
        self.J = j
        self.K = k
        self.Length = self.get_length(0, i, 0, j, 0, k)
        self.UnitVector = self.get_unit_vector()

    def get_length(self, i, ii, j, jj, k, kk):
        return_length = sqrt(pow((ii - i), 2) +
                             pow((jj - j), 2) +
                             pow((kk - k), 2))
        return return_length

    def get_unit_vector(self):
        return_vector = Vector((self.I / self.Length), (self.J / self.Length), (self.K / self.Length))
        return return_vector