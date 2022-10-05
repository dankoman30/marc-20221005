class Color:
    # default values
    R = 255
    G = 255
    B = 255

    def __init__(self, *args):
        if (len(args) == 3) and all(isinstance(value, int) for value in args):  # 3 integers passed
            self.R = args[0]
            self.G = args[1]
            self.B = args[2]




