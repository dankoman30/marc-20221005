from math import sqrt


class Vector:
    def __int__(self):
        self.I = 0
        self.J = 0
        self.K = 1
        self.Length = 1
        self.UnitVector = self.get_unit_vector()

    def __init__(self, i, j, k):
        self.I = i
        self.J = j
        self.K = k
        self.Length = self.get_length(0, i, 0, j, 0, k)
        self.UnitVector = self.get_unit_vector()

    def __init__(self, point):
        self.I = point.X
        self.J = point.Y
        self.K = point.Z
        self.Length = self.get_length(0, point.X, 0, point.Y, 0, point.Z)
        self.UnitVector = self.get_unit_vector()

    def __init__(self, point1, point2):
        self.I = point2.X - point1.X
        self.J = point2.Y - point1.Y
        self.K = point2.Z - point1.Z
        self.Length = self.get_length(point2.X, point1.X, point2.Y, point1.Y, point2.Z, point1.Z)
        self.UnitVector = self.get_unit_vector()

    def get_length(self, i, ii, j, jj, k, kk):
        return_length = sqrt(pow((ii - i), 2) +
                             pow((jj - j), 2) +
                             pow((kk - k), 2))
        return return_length

    def get_unit_vector(self):
        return_vector = Vector((self.I / self.Length), (self.J / self.Length), (self.K / self.Length))
        return return_vector