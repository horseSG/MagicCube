
from enum import Enum

class FacetOrientation(Enum):
    Front = 0
    Back = 1
    Up = 2
    Down = 3
    Left = 4
    Right = 5

    def iniColor(self):
        if self == FacetOrientation.Front:
            return 'blue'
        elif self == FacetOrientation.Back:
            return 'green'
        elif self == FacetOrientation.Up:
            return 'yellow'
        elif self == FacetOrientation.Down:
            return 'white'
        elif self == FacetOrientation.Left:
            return 'orange'
        else:
            return 'red'

class Facet:
    def __init__(self, orientation, v0, v1, v2, v3):
        self.Orientation = orientation
        self.Verts = [v0, v1, v2, v3]
        self.Color = orientation.iniColor()
        self.OldColor = None

    def BackupColor(self):
        self.OldColor = self.Color

    def RecvColor(self, color):
        # self.OldColor = self.Color
        self.Color = color

# Location type

# value is number of facets
class PieceType(Enum):
    Center = 0
    FaceCent = 1
    EdgeMid = 2
    Vert = 3

    @classmethod
    def from_location(cls, location):
        num_zero = location.count(0)
        if num_zero == 3:
            return cls.Center
        elif num_zero == 2:
            return cls.FaceCent
        elif num_zero == 0:
            return cls.Vert
        else:
            return cls.EdgeMid

class Piece:
    def __init__(self, xid, yid, zid):      # x/y/zid: (-1, 0, 1)
        self.Location = [xid, yid, zid]
        self.Type = PieceType.from_location(self.Location)
        self.Facets = []
        self.OriDict = {}
        self.Add_facets()       # set facets' verts
        if self.Type.value != len(self.Facets):     # check number of facets
            raise ValueError(f"Location: ({xid}, {yid}, {zid})\nPiece type: {self.Type}\nnumber of facets: {len(self.Facets)}")
        self.Send = False
        self.Recv = False

    def Add_facets(self):
        numFacets = self.Type.value
        xid = self.Location[0]
        yid = self.Location[1]
        zid = self.Location[2]
        # Back/Front Facet
        if xid == -1 or xid == 1:
            if xid == -1:
                tx = -1.5
                tori = FacetOrientation.Back
            else:
                tx = 1.5
                tori = FacetOrientation.Front
            ty = yid - 0.5
            tz = zid - 0.5
            v0 = [tx, ty, tz]         # yid, zid also needs to adjust with 0.5
            v1 = [tx, ty+1, tz]
            v2 = [tx, ty+1, tz+1]
            v3 = [tx, ty, tz+1]
            self.Facets.append(Facet(tori, v0, v1, v2, v3))
            self.OriDict[tori] = self.Facets[-1]

        # Left/Right Facet
        if yid == -1 or yid == 1:
            if yid == -1:
                ty = -1.5
                tori = FacetOrientation.Left
            else:
                ty = 1.5
                tori = FacetOrientation.Right
            tx = xid - 0.5
            tz = zid - 0.5
            v0 = [tx, ty, tz]
            v1 = [tx+1, ty, tz]
            v2 = [tx+1, ty, tz+1]
            v3 = [tx, ty, tz+1]
            self.Facets.append(Facet(tori, v0, v1, v2, v3))
            self.OriDict[tori] = self.Facets[-1]

        # Up/Down Facet
        if zid == -1 or zid == 1:
            if zid == -1:
                tz = -1.5
                tori = FacetOrientation.Down
            else:
                tz = 1.5
                tori = FacetOrientation.Up
            tx = xid - 0.5
            ty = yid - 0.5
            v0 = [tx, ty, tz]
            v1 = [tx+1, ty, tz]
            v2 = [tx+1, ty+1, tz]
            v3 = [tx, ty+1, tz]
            self.Facets.append(Facet(tori, v0, v1, v2, v3))
            self.OriDict[tori] = self.Facets[-1]

    def BackupColors(self):
        for facet in self.Facets:
            facet.BackupColor()
