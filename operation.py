
from component import FacetOrientation as fo

class RotUpper:
    def __init__(self):
        self.ChangeDim = (0, 1)     # dimension (x, y)
        self.FixLayer = (2, 1)      # (dimision-z, z=1)
        self.RotMat = [[0, 1], [-1, 0]]
        self.Conv_FacetOri = {
            fo.Back: fo.Right,
            fo.Right: fo.Front,
            fo.Front: fo.Left,
            fo.Left: fo.Back,
            fo.Up: fo.Up,
            fo.Down: fo.Down
        }

class RotUpperPrime:
    def __init__(self):
        self.ChangeDim = (0, 1)     # dimension (x, y)
        self.FixLayer = (2, 1)      # (dimision-z, z=1)
        self.RotMat = [[0, -1], [1, 0]]
        self.Conv_FacetOri = {
            fo.Back: fo.Left,
            fo.Right: fo.Back,
            fo.Front: fo.Right,
            fo.Left: fo.Front,
            fo.Up: fo.Up,
            fo.Down: fo.Down
        }